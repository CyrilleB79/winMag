# -*- coding: UTF-8 -*-
# globalPlugins/winMag/__init__.py
# NVDA add-on: Windows Magnifier
# Copyright (C) 2019-2023 Cyrille Bougot
# This file is covered by the GNU General Public License.
# See the file COPYING.txt for more details.

from __future__ import unicode_literals

from .wmGui import WinMagSettingsPanel
from .utils import (
	magnifierDefaultValuesMapping,
	getMagnifierKeyValue,
	setMagnifierKeyValue,
	toggleMagnifierKeyValue,
	isMagnifierRunning,
	getMagnifierUIWindow,
	getDockedWindowObject,
	getLensWindowObject,
	isScreenCurtainActive,
)
from .msg import nvdaTranslation
from .magnification import Magnification
from . import winUser2

import globalPluginHandler
import appModuleHandler
import ui
import gui.settingsDialogs
import scriptHandler
import api
from tones import beep
from scriptHandler import script
from logHandler import log
import mouseHandler
import globalVars
import winUser
from keyboardHandler import KeyboardInputGesture
from keyLabels import localizedKeyLabels
import config
import core
import NVDAObjects.IAccessible
import controlTypes

import wx

import sys

import time
from functools import wraps
from types import MethodType

import addonHandler

addonHandler.initTranslation()


# Magnifier view types
MAG_VIEW_DOCKED = 1
MAG_VIEW_FULLSCREEN = 2
MAG_VIEW_LENS = 3

confspec = {
	"reportViewMove": 'option("off", "speech", "tones", default="off")',
	"reportMoveToScreenEdges": 'option("off", "speech", "tones", default="off")',
	"toneVolume": 'integer(default=50,min=1,max=100)',
	"reportTurnOnOff": "boolean(default=True)",
	"reportZoom": "boolean(default=True)",
	"reportColorInversion": "boolean(default=True)",
	"reportViewChange": "boolean(default=True)",
	"reportLensResizing": "boolean(default=False)",
	"passCtrlAltArrow": 'option("never", "whenNotInTable", "always", default="never")',
	"keepWindowAlwaysOnTop": "boolean(default=True)",
	"magnifierConfig": {
		k: "integer(default={})".format(v) for (k, v) in magnifierDefaultValuesMapping.items()
	},
}
config.conf.spec["winMag"] = confspec


ADDON_SUMMARY = addonHandler.getCodeAddon().manifest["summary"]

# Alpha-numeric keyboard Magnifier keys
# Translators: The key used natively byt the Magnifier on the alpha-numeric (main) keyboard in conjunction
# with Win key to zoom in.
KEY_ALPHA_PLUS = _("=")
# Translators: The key used natively byt the Magnifier on the alpha-numeric (main) keyboard in conjunction
# with Win key to zoom out.
KEY_ALPHA_MINUS = _("-")

# Check of these translated keys:
# Do not do it in GlobalPlugin.__init__ since these strings are used at class definition.
if KEY_ALPHA_PLUS == "+":
	KEY_ALPHA_PLUS == "plus"
if (
	(len(KEY_ALPHA_PLUS) != 1 and KEY_ALPHA_PLUS != 'plus')
	or len(KEY_ALPHA_MINUS) != 1
):
	log.error("Error in Windows Magnifier shortcut key translation (Windows Magnifier add-on)")


def getMagViewMode():
	return getMagnifierKeyValue('MagnificationMode')


def onlyIfMagRunning(s):
	"""This script decorator allows the decorated script to execute only if the Magnifier is active.
	If not a message informs the user that the Magnifier is not running.
	"""

	@wraps(s)
	def script_wrapper(self, gesture):
		if not isMagnifierRunning():
			# Translators: The message reported when the user tries to use a Magnifier dedicated command
			# while the Magnifier is not running.
			ui.message(_('The Magnifier is not active'))
			return
		s(self, gesture)
	return script_wrapper


def onlyIfDockedOrFullScreenView(s):
	"""This script decorator allows the decorated script to execute only if docked or full screen view is active.
	If not a message informs the user that the feature is not available only in docked or full screen view.
	"""

	@wraps(s)
	def script_wrapper(self, gesture):
		mode = getMagViewMode()
		if mode not in [MAG_VIEW_FULLSCREEN, MAG_VIEW_DOCKED]:
			# Translators: The message reported when the user tries to toggle a tracking mode while docked
			# or full screen view is not active.
			ui.message(_('Tracking configuration only applicable with docked or full screen view.'))
			return
		s(self, gesture)
	return script_wrapper


# Below toggle code came from Tyler Spivey's code, with enhancements by Joseph Lee.
def finally_(func, final):
	"""Calls final after func, even if it fails."""
	def wrap(f):
		@wraps(f)
		def new(*args, **kwargs):
			try:
				func(*args, **kwargs)
			finally:
				final()
		return new
	return wrap(final)


# Code taken from NVDA's source code NVDAObjects/window/winword.py
def _WaitForValueChangeForAction(gesture, fetcher, timeout=0.2, sleepTime=0.03):
	oldVal = fetcher()
	gesture.send()
	startTime = curTime = time.time()
	while (curTime - startTime) < timeout:
		curVal = fetcher()
		if curVal != oldVal:
			return curVal
		time.sleep(sleepTime)
		curTime = time.time()
	log.warning('No value change detected')
	return curVal


class NotInTableException(Exception):
	pass


def createScriptForControlAltArrow(originalScript):
	"""A factory function creating a compound script from an original one.
	According to the config, the compound script may call magnifier move commands only when not in a table
	or even in any situation, i.e. even when in a table.

	This function should not be called when config.conf['winMag']['passCtrlAltArrow'] == 'never'
	since the script normally identified by NVDA should be returned by findScript in this case.
	"""

	@wraps(originalScript)
	def scriptControlAltArrow(self, g):
		global canRaiseNotInTableException
		if config.conf['winMag']['passCtrlAltArrow'] == 'always':
			executeMoveScript = True
		if config.conf['winMag']['passCtrlAltArrow'] == 'whenNotInTable':
			try:
				canRaiseNotInTableException = True
				originalScript(g)
				executeMoveScript = False
			except NotInTableException:
				executeMoveScript = True
			finally:
				canRaiseNotInTableException = False
		if executeMoveScript:
			winMagPlugin = [p for p in globalPluginHandler.runningPlugins if isinstance(p, GlobalPlugin)][0]
			winMagPlugin.script_moveView(g)
	try:
		return MethodType(scriptControlAltArrow, originalScript.__self__)
	except AttributeError:
		# originalScript.__self__ is not defined if originalScript is a function and not a bound method
		# This can happen in some addons' implementation of layered command
		# as well as the following definition in gestures.ini:
		# kb:a = kb:b
		# No patch in this case
		return originalScript


canRaiseNotInTableException = False
orig_findScript = scriptHandler.findScript
orig_message = ui.message
cached = {}


def patched_findScript(gesture):
	global cached
	oldScript = orig_findScript(gesture)
	try:
		mainKeyName = gesture.mainKeyName
	except AttributeError:
		# This gesture is not a KeyboardInputGesture, so mainKeyName attribut does not exist
		mainKeyName = None

	winMagPlugin = [p for p in globalPluginHandler.runningPlugins if isinstance(p, GlobalPlugin)][0]
	if mainKeyName and mainKeyName.endswith('Arrow'):
		# Control+shift+arrows is caught by Magnifier when it is running to resize lens or docked windows.
		# Else it may correspond to another shortcut such as in Word where these gesture are the one
		# to increase/decrease title level or to move up/down a paragraph.
		if (
			config.conf['winMag']['reportLensResizing']
			and gesture.normalizedIdentifiers[0].split(':')[1] in [
				'alt+downarrow+shift',
				'alt+leftarrow+shift',
				'alt+rightarrow+shift',
				'alt+shift+uparrow',
			]
			and isMagnifierRunning()
		):
			return winMagPlugin.script_changeMagnificationWindowSize
		# For control+alt+arrow, create a compound script:
		# that will call Magnifier move commands (control+alt+arrow) rather than saying "Not in a table" message.
		if (
			config.conf['winMag']['passCtrlAltArrow'] != 'never'
			and gesture.normalizedIdentifiers[0].split(':')[1] in [
				'alt+control+downarrow',
				'alt+control+leftarrow',
				'alt+control+rightarrow',
				'alt+control+uparrow',
			]
			and isMagnifierRunning()
		):
			if oldScript:
				# We need a cache so that, for last script, checking wrapped script has always the same ref
				# else, getLastScriptRepeatCount would always return 0
				newScript = cached.get(oldScript, None)
				if not newScript:
					try:
						newScript = createScriptForControlAltArrow(oldScript)
					except Exception:
						# If patching fails for any reason, log the error, but also return oldScript in order not to block NVDA.
						newScript = oldScript
						log.exception('Error patching script')
					cached = {oldScript: newScript}
				return newScript
			else:
				return winMagPlugin.script_moveView
	return oldScript


def patched_message(text, *args, **kwargs):
	if canRaiseNotInTableException:
		if (
			text in [nvdaTranslation(m) for m in ['Not in table', 'Not in a table cell']]
			and isMagnifierRunning()
		):
			raise NotInTableException
	orig_message(text, *args, **kwargs)


class TrackingConfig(object):

	TRACKING_KEY_NAME_MAPPING = {
		# Translators: A UI object that can be tracked (followed) by the Magnifier.
		# If possible, translate with the term used in Magnifier's options.
		'FollowMouse': _('Mouse pointer'),
		# Translators: A UI object that can be tracked (followed) by the Magnifier.
		# If possible, translate with the term used in Magnifier's options.
		'FollowFocus': _('Keyboard focus'),
		# Translators: A UI object that can be tracked (followed) by the Magnifier.
		# If possible, translate with the term used in Magnifier's options.
		'FollowCaret': _('Text cursor'),
	}
	lastTrackingConfig = None

	def toggle(self, eventType):
		cfg = {k: getMagnifierKeyValue(k) for k in self.TRACKING_KEY_NAME_MAPPING.keys()}
		if any(cfg.values()):
			self.__class__.lastTrackingConfig = dict(cfg)
		if eventType == 'All':
			if any(cfg.values()):
				cfg = {n: 0 for n in cfg.keys()}
				val = 0
			else:
				lastCfg = self.__class__.lastTrackingConfig
				cfg = lastCfg if lastCfg is not None else {n: 1 for n in cfg.keys()}
				val = 1
			names = cfg.keys()
		else:
			val = 0 if cfg[eventType] else 1
			cfg[eventType] = val
			names = [eventType]
		for n in names:
			setMagnifierKeyValue(n, cfg[n])
		if any(cfg.values()):
			self.__class__.lastTrackingConfig = dict(cfg)
		return val


# Translators: The description of a command of this add-on.
DESC_TOGGLE_CARET_TRACKING = _("Toggles on or off caret tracking")
# Translators: The description of a command of this add-on.
DESC_TOGGLE_FOCUS_TRACKING = _("Toggles on or off focus tracking")
# Translators: The description of a command of this add-on.
DESC_TOGGLE_MOUSE_TRACKING = _("Toggles on or off mouse tracking")
# Translators: The description of a command of this add-on.
DESC_TOGGLE_TRACKING = _("Toggles on or off tracking globally")
# Translators: The description of a command of this add-on.
DESC_TOGGLE_SMOOTHING = _("Toggles on or off smoothing")
DESC_TOGGLE_MOUSE_CURSOR_TRACKING_MODE = _(
	# Translators: The description of a command of this add-on.
	"Switches between mouse pointer tracking modes (within the edge of the screen or centered on the screen)"
)
DESC_TOGGLE_TEXT_CURSOR_TRACKING_MODE = _(
	# Translators: The description of a command of this add-on.
	"Switches between text tracking modes (within the edge of the screen or centered on the screen)"
)
DESC_SAVE_MAGNIFIER_CONFIG = _(
	# Translators: The description of a command of this add-on.
	"Saves the current configuration parameters of the magnifier to NVDA's configuration."
)
DESC_RESTORE_MAGNIFIER_CONFIG = _(
	# Translators: The description of a command of this add-on.
	"Restores the current configuration parameters of the magnifier from NVDA's configuration."
)
# Translators: The description of a command of this add-on.
DESC_MOVE_VIEW = _("Moves the magnified view")
# Translators: The description of a command of this add-on.
DESC_MOVE_MOUSE_TO_VIEW = _("Moves the mouse cursor in the center of the zoomed view")
DESC_KEEP_MAG_WINDOW_ON_TOP = _(
	# Translators: The description of a command of this add-on.
	"Switches on or off the mode keeping Windows Magnifier's control window always on top of the other ones."
)
# Translators: The description of a command of this add-on.
DESC_OPEN_SETTINGS = _("Opens Windows Magnifier add-on settings")
# Translators: The description of a command of this add-on.
DESC_DISPLAY_HELP = _("Displays help on Magnifier layer commands")


class Screen(object):
	def __init__(self, width, height, minPos):
		self.width = width
		self.height = height
		self.minPos = minPos

	@classmethod
	def getCurrentScreen(cls):
		"""Create an instance from the current screen.
		"""
		if wx.Display.GetCount() != 1:
			ui.message(
				# Translators: A message reported when the user tries to execute a script in multi-screen setup.
				_('Multi-screen setup not yet supported. Please contact the add-on author to have it implemented.')
			)
			raise NotImplementedError('Multi-screen environment not yet implemented. Please contact add-on author.')
		displays = [wx.Display(i).GetGeometry() for i in range(wx.Display.GetCount())]
		width, height, minPos = mouseHandler.getTotalWidthAndHeightAndMinimumPosition(displays)
		return cls(width, height, minPos)


class View(object):
	def __init__(self, screen, mode):
		self.screen = screen
		self.mode = mode

	@property
	def width(self):
		raise NotImplementedError

	@property
	def height(self):
		raise NotImplementedError

	def positionInScreen(self):
		"""Position of the view with respect to the possibility to move it in the screen.
		"""
		raise NotImplementedError

	def centerPositionInScreen(self):
		""" Position of the center of the view in the screen.
		"""
		raise NotImplementedError

	@staticmethod
	def getCurrentView(mode):
		screen = Screen.getCurrentScreen()
		if mode == MAG_VIEW_FULLSCREEN:
			try:
				Magnification.MagInitialize()
				zoomLevel, left, top = Magnification.MagGetFullscreenTransform()
			finally:
				Magnification.MagUninitialize()
			return FullscreenView(screen, zoomLevel=zoomLevel, left=left, top=top)
		elif mode == MAG_VIEW_LENS:
			window = getLensWindowObject()
			return LensView(screen, window=window)
		else:
			raise NotImplementedError

	def isAtEdge(self, orientation):
		raise NotImplementedError


class FullscreenView(View):
	def __init__(self, screen, zoomLevel, left, top):
		super(FullscreenView, self).__init__(screen, MAG_VIEW_FULLSCREEN)
		self.zoomLevel = zoomLevel
		self.left = left
		self.top = top

	@property
	def width(self):
		return self.screen.width / self.zoomLevel

	@property
	def height(self):
		return self.screen.height / self.zoomLevel

	def positionInScreen(self):
		if self.zoomLevel == 1:
			return 0.5, 0.5
		minX, minY = self.screen.minPos
		# log.debug(f'minX={minX}; viewLeft={self.left}; screenWidth={self.screen.width}; viewWidth={self.width}')
		# log.debug(f'minY={minY}; viewTop={self.top}; screenHeight={self.screen.height}; viewHeight={self.height}')
		x = (self.left - minX) / (self.screen.width - self.width)
		y = (self.top - minY) / (self.screen.height - self.height)
		return x, y

	def centerPositionInScreen(self):
		x = self.left + int(self.width / 2)
		y = self.top + int(self.height / 2)
		return x, y

	def isAtEdge(self, orientation):
		isAtTopEdge = orientation == 'up' and self.top == 0
		isAtLeftEdge = orientation == 'left' and self.left == 0
		isAtBottomEdge = orientation == 'down' and self.top + 1 >= self.screen.height * (1 - 1 / self.zoomLevel)
		isAtRightEdge = orientation == 'right' and self.left + 1 >= self.screen.width * (1 - 1 / self.zoomLevel)
		return (
			self.zoomLevel == 1
			or isAtTopEdge
			or isAtLeftEdge
			or isAtBottomEdge
			or isAtRightEdge
		)


class LensView(View):
	def __init__(self, screen, window):
		super(LensView, self).__init__(screen, MAG_VIEW_LENS)
		self.window = window

	def positionInScreen(self):
		x, y = self.window.location.center
		xPc = (x - 1) / (self.screen.width - 2)
		yPc = (y - 1) / (self.screen.height - 2)
		return xPc, yPc

	def centerPositionInScreen(self):
		x, y = self.window.location.center
		return x, y

	def isAtEdge(self, orientation):
		x, y = self.window.location.center
		isAtTopEdge = orientation == 'up' and y <= 1
		isAtLeftEdge = orientation == 'left' and x <= 1
		isAtBottomEdge = orientation == 'down' and y >= self.screen.height - 1
		isAtRightEdge = orientation == 'right' and x >= self.screen.width - 1
		return (
			isAtTopEdge
			or isAtLeftEdge
			or isAtBottomEdge
			or isAtRightEdge
		)


class VolumeSlider(NVDAObjects.IAccessible.IAccessible):
	"""A class that discard value reporting on value change.
	This class is meant to be used with a volume slider that produces a beep on value change.
	"""

	def event_valueChange(self):
		pass


def enableProfileTriggersAndActivate():
	"""Enable profile triggers after they have been disabled
	and activate the profile of the currently focused application if any.
	"""
	# Code copied from NVDA globalCommands.py

	config.conf.enableProfileTriggers()
	# Explicitly trigger profiles for the current application.
	mod = api.getForegroundObject().appModule
	trigger = mod._configProfileTrigger = appModuleHandler.AppProfileTrigger(mod.appName)
	trigger.enter()


class GlobalPlugin(globalPluginHandler.GlobalPlugin):

	scriptCategory = ADDON_SUMMARY

	__magLayerCommandList = [
		(["c"], "toggleCaretTracking", DESC_TOGGLE_CARET_TRACKING),
		(["f"], "toggleFocusTracking", DESC_TOGGLE_FOCUS_TRACKING),
		(["m"], "toggleMouseTracking", DESC_TOGGLE_MOUSE_TRACKING),
		(["t"], "toggleTracking", DESC_TOGGLE_TRACKING),
		(["s"], "toggleSmoothing", DESC_TOGGLE_SMOOTHING),
		(["r"], "toggleMouseCursorTrackingMode", DESC_TOGGLE_MOUSE_CURSOR_TRACKING_MODE),
		(["x"], "toggleTextCursorTrackingMode", DESC_TOGGLE_TEXT_CURSOR_TRACKING_MODE),
		(["shift+p"], "saveMagnifierConfig", DESC_SAVE_MAGNIFIER_CONFIG),
		(["p"], "restoreMagnifierConfig", DESC_RESTORE_MAGNIFIER_CONFIG),
		(["upArrow", "downArrow", "leftArrow", "rightArrow"], "moveViewLayeredCommand", DESC_MOVE_VIEW),
		(["v"], "moveMouseToView", DESC_MOVE_MOUSE_TO_VIEW),
		(["w"], "keepMagWindowOnTop", DESC_KEEP_MAG_WINDOW_ON_TOP),
		(["o"], "openSettings", DESC_OPEN_SETTINGS),
		(["h"], "displayHelp", DESC_DISPLAY_HELP),
	]

	isWinMagPlugin = True

	def __init__(self):
		super(GlobalPlugin, self).__init__()

		# Variable initializations
		self.toggling = False
		self.lastResize = None
		self.lastMoveDirection = None
		self.reportViewTimer = None

		# Gui initialization
		gui.settingsDialogs.NVDASettingsDialog.categoryClasses.append(WinMagSettingsPanel)

		self.updateKeepMagWindowOnTop(config.conf['winMag']['keepWindowAlwaysOnTop'])

		# Patched functions
		ui.message = patched_message
		scriptHandler.findScript = patched_findScript

		# Extension points configuration
		config.post_configProfileSwitch.register(self.handleConfigProfileSwitch)
		config.post_configReset.register(self.handleConfigReload)

	def chooseNVDAObjectOverlayClasses(self, obj, clsList):
		if (
			obj.windowClassName == 'msctls_trackbar32'
			and obj.role == controlTypes.Role.SLIDER
			and NVDAObjects.IAccessible.IAccessible in clsList
		):
			try:
				panel = obj.parent.parent
			except AttributeError:
				return
			if panel.name == ADDON_SUMMARY:
				clsList.insert(0, VolumeSlider)

	def getScript(self, gesture):
		if not self.toggling:
			return globalPluginHandler.GlobalPlugin.getScript(self, gesture)
		script = globalPluginHandler.GlobalPlugin.getScript(self, gesture)
		if not script:
			script = finally_(self.script_error, self.finish)
		if getattr(script, 'allowMultipleLayeredCommands', None):
			return script
		else:
			return finally_(script, self.finish)

	def finish(self):
		self.toggling = False
		self.clearGestureBindings()
		self.bindGestures(self.__gestures)

	def script_error(self, gesture):
		beep(120, 100)

	@script(
		# Translators: Part of the description for the layered command script.
		description=_("Windows Magnifier layer commands entry point."),
		gesture="kb:NVDA+windows+O",
	)
	@onlyIfMagRunning
	def script_magLayer(self, gesture):
		# A run-time binding will occur from which we can perform various layered commands.
		# First, check if a second press of the script was done.
		if self.toggling:
			self.script_error(gesture)
			return
		layerGestures = {}
		for (gestures, command, desc) in self.__magLayerCommandList:
			for g in gestures:
				layerGestures["kb:" + g] = command
		self.bindGestures(layerGestures)
		self.toggling = True
		beep(100, 10)

	def terminate(self):
		ui.message = orig_message
		scriptHandler.findScript = orig_findScript
		try:
			self.updateKeepMagWindowOnTop(True)  # Restore to default behaviour.
		except Exception:
			log.error('Error restoring Magnifier window on top.', exc_info=True)
		gui.settingsDialogs.NVDASettingsDialog.categoryClasses.remove(WinMagSettingsPanel)
		config.post_configProfileSwitch.unregister(self.handleConfigProfileSwitch)
		config.post_configReset.unregister(self.handleConfigReload)
		super(GlobalPlugin, self).terminate()

	def handleConfigProfileSwitch(self):
		self.updateKeepMagWindowOnTop(config.conf['winMag']['keepWindowAlwaysOnTop'])

	def handleConfigReload(self, factoryDefaults=False):
		self.updateKeepMagWindowOnTop(config.conf['winMag']['keepWindowAlwaysOnTop'])

	@script(
		gestures=[
			"kb:windows+numpadPlus",
			"kb:windows+numLock+numpadPlus",
			"kb:windows+" + KEY_ALPHA_PLUS,
			"kb:windows+plus",
		],
	)
	def script_zoomIn(self, gesture):
		numlockWasOn = 'numlock' in gesture.normalizedIdentifiers[0].split(':')[1]
		if config.conf['winMag']['reportZoom'] and isMagnifierRunning():
			self.modifyZoomLevel(gesture)
		elif not isMagnifierRunning():
			if config.conf['winMag']['reportTurnOnOff']:
				self.modifyRunningState(gesture)
			else:
				gesture.send()
			core.callLater(200, lambda: self.updateKeepMagWindowOnTop(config.conf['winMag']['keepWindowAlwaysOnTop']))
		else:
			gesture.send()
		if numlockWasOn:
			# A gesture.send() with numlock on will unwantedly toggle numlock (see NVDA issue #10827), so restore it.
			KeyboardInputGesture.fromName('numlock').send()

	@script(
		gestures=[
			"kb:windows+numpadMinus",
			"kb:windows+numLock+numpadMinus",
			"kb:windows+" + KEY_ALPHA_MINUS,
			"kb:windows+-",
		],
	)
	def script_zoomOut(self, gesture):
		numlockWasOn = 'numlock' in gesture.normalizedIdentifiers[0].split(':')[1]
		if config.conf['winMag']['reportZoom'] and isMagnifierRunning():
			self.modifyZoomLevel(gesture)
		else:
			gesture.send()
		if numlockWasOn:
			# A gesture.send() with numlock on will unwantedly toggle numlock (see NVDA issue #10827), so restore it.
			KeyboardInputGesture.fromName('numlock').send()

	@script(
		gesture="kb:windows+escape",
	)
	def script_quitMagnifier(self, gesture):
		if config.conf['winMag']['reportTurnOnOff'] and isMagnifierRunning():
			self.modifyRunningState(gesture)
		else:
			gesture.send()

	@script(
		gesture="kb:control+alt+I",
	)
	def script_toggleColorInversion(self, gesture):
		if config.conf['winMag']['reportColorInversion'] and isMagnifierRunning():
			self.modifyColorInversion(gesture)
		else:
			gesture.send()

	@script(
		gestures=["kb:control+alt+M", "kb:control+alt+D", "kb:control+alt+F", "kb:control+alt+L"],
	)
	def script_changeMagnificationView(self, gesture):
		if isMagnifierRunning():
			if config.conf['winMag']['reportViewChange']:
				self.modifyMagnificationView(gesture)
			else:
				gesture.send()
			time.sleep(0.5)
			self.updateKeepMagWindowOnTop(config.conf['winMag']['keepWindowAlwaysOnTop'])
		else:
			gesture.send()

	def script_moveView(self, gesture):
		self.report_viewMove(gesture)

	def report_viewMove(self, gesture):
		gesture.send()
		reportMoves = config.conf['winMag']['reportViewMove'] != 'off'
		reportEdges = config.conf['winMag']['reportMoveToScreenEdges'] != 'off'
		if not (reportMoves or reportEdges):
			return
		mode = getMagViewMode()
		if (
			# No implementation has been found to report view position in docked mode
			mode == MAG_VIEW_DOCKED
			# Calling Magnification.MagGetFullscreenTransform causes unwanted deactivation (crash) of screen curtain.
			or (mode == MAG_VIEW_FULLSCREEN and isScreenCurtainActive())
		):
			return

		# Cancel previously scheduled position reporting.
		try:
			self.reportViewTimer.Stop()
			self.reportViewTimer = None
		except AttributeError:
			pass

		if gesture.mainKeyName in ['leftArrow', 'rightArrow']:
			direction = 'horizontal'
		elif gesture.mainKeyName in ['upArrow', 'downArrow']:
			direction = 'vertical'
		else:
			raise RuntimeError('Unexpected key name {key}'.format(key=gesture.mainKeyName))
		orientation = gesture.mainKeyName[:-len('Arrow')]

		view = View.getCurrentView(mode)
		isAtEdge = view.isAtEdge(orientation)
		if isAtEdge:
			if reportEdges:
				self.reportScreenEdge()
			elif reportMoves:
				self.report_viewPosition(direction, view)
			return

		if reportMoves:
			# Report view move immediately only if it is the second keypress in the same direction.
			if scriptHandler.getLastScriptRepeatCount() > 0 and direction == self.lastMoveDirection:
				self.report_viewPosition(direction, view)

			# Schedule position reporting when the view has finished moving.
			# wx.CallLater is used rather than core.callLater to avoid having tones reporting position
			# after tones reporting screen edge in some cases.
			self.lastMoveDirection = direction

			def reportViewPositionHelper():
				view = View.getCurrentView(mode)
				self.report_viewPosition(direction, view)
			self.reportViewTimer = wx.CallLater(300, reportViewPositionHelper)

	def reportScreenEdge(self):
		if config.conf['winMag']['reportMoveToScreenEdges'] == 'speech':
			# Translators: A message reported when the user reaches the edge of the screen while moving the view.
			ui.message(_('Edge of the screen.'))
		elif config.conf['winMag']['reportMoveToScreenEdges'] == 'tones':
			# Compute the pitch for the note 2 tones above max coordinate pitch.
			edgePitch = config.conf['mouse']['audioCoordinates_maxPitch'] * 2 ** (4 / 12)
			vol = config.conf['winMag']['toneVolume']
			beep(edgePitch, 30, vol, vol)
			time.sleep(0.06)
			beep(edgePitch, 30, vol, vol)
		else:
			raise RuntimeError('Unexpected config {config}'.format(config=config.conf['winMag']['reportViewMove']))

	def report_viewPosition(self, direction, view):
		x, y = view.positionInScreen()
		if direction == 'horizontal':
			val = x
		elif direction == 'vertical':
			val = y
		if config.conf['winMag']['reportViewMove'] == 'speech':
			if view.mode == MAG_VIEW_FULLSCREEN and view.zoomLevel < 4:
				precision = 0
			else:
				precision = 1
			if precision == 1:
				msg = '{val:.1f}%'
			else:
				msg = '{val:.0f}%'
			ui.message(msg.format(val=round(val * 100, precision)))
		elif config.conf['winMag']['reportViewMove'] == 'tones':
			if direction == 'vertical':
				val = 1 - val
			minPitch = config.conf['mouse']['audioCoordinates_minPitch']
			maxPitch = config.conf['mouse']['audioCoordinates_maxPitch']
			curPitch = minPitch + ((maxPitch - minPitch) * val)
			vol = config.conf['winMag']['toneVolume']
			beep(curPitch, 40, vol, vol)

	def script_changeMagnificationWindowSize(self, gesture):
		if isMagnifierRunning():
			gesture.send()
			mode = getMagViewMode()
			if mode == MAG_VIEW_DOCKED:
				oMag = getDockedWindowObject()
				curResize = 'width' if gesture.mainKeyName in ['leftArrow', 'rightArrow'] else 'height'
				announceDim = curResize != self.lastResize or not scriptHandler.getLastScriptRepeatCount()
				msg = '{dimension}: {val}' if announceDim else '{val}'
				if curResize == 'width':
					# Translators: A dimension reported when the user resizes the docked view.
					dim = _('Widht')
					val = oMag.location.width
					self.lastResize = 'width'
				elif curResize == 'height':
					# Translators: A dimension reported when the user resizes the docked view.
					dim = _('Height')
					val = oMag.location.height
					self.lastResize = 'height'
				ui.message(msg.format(dimension=dim, val=val))
			elif mode == MAG_VIEW_LENS:
				# Translators: A message reported when the user resizes the lens with the keyboard.
				ui.message(_('Resizing lens.'))
			else:
				# Translators: A message reported when the user uses resizing shortcuts (control+shift+arrow)
				# in full screen view.
				ui.message(_('Resizing not available in full screen.'))
		else:
			raise RuntimeError('Unexpected case')

	@script(
		description=DESC_TOGGLE_CARET_TRACKING,
	)
	@onlyIfMagRunning
	@onlyIfDockedOrFullScreenView
	def script_toggleCaretTracking(self, gesture):
		if self.checkSecureScreen():
			return
		cfg = TrackingConfig()
		val = cfg.toggle('FollowCaret')
		if val:
			# Translators: The message reported when the user turns on caret tracking.
			ui.message(_('Caret tracking on'))
		else:
			# Translators: The message reported when the user turns off caret tracking.
			ui.message(_('Caret tracking off'))

	@script(
		description=DESC_TOGGLE_FOCUS_TRACKING,
	)
	@onlyIfMagRunning
	@onlyIfDockedOrFullScreenView
	def script_toggleFocusTracking(self, gesture):
		if self.checkSecureScreen():
			return
		cfg = TrackingConfig()
		val = cfg.toggle('FollowFocus')
		if val:
			# Translators: The message reported when the user turns on focus tracking.
			ui.message(_('Focus tracking on'))
		else:
			# Translators: The message reported when the user turns off focus tracking.
			ui.message(_('Focus tracking off'))

	@script(
		description=DESC_TOGGLE_MOUSE_TRACKING,
	)
	@onlyIfMagRunning
	@onlyIfDockedOrFullScreenView
	def script_toggleMouseTracking(self, gesture):
		if self.checkSecureScreen():
			return
		cfg = TrackingConfig()
		val = cfg.toggle('FollowMouse')
		if val:
			# Translators: The message reported when the user turns on mouse tracking.
			ui.message(_('Mouse tracking on'))
		else:
			# Translators: The message reported when the user turns off focus tracking.
			ui.message(_('Mouse tracking off'))

	@script(
		description=DESC_TOGGLE_TRACKING,
	)
	@onlyIfMagRunning
	@onlyIfDockedOrFullScreenView
	def script_toggleTracking(self, gesture):
		if self.checkSecureScreen():
			return
		cfg = TrackingConfig()
		val = cfg.toggle('All')
		if val:
			# Translators: The message reported when the user turns on tracking.
			ui.message(_('Tracking on - {trackingTypes}').format(trackingTypes=', '.join(
				cfg.TRACKING_KEY_NAME_MAPPING[c] for c, v in cfg.lastTrackingConfig.items() if v
			)))
		else:
			# Translators: The message reported when the user turns off tracking.
			ui.message(_('Tracking off'))

	@script(
		description=DESC_TOGGLE_SMOOTHING,
	)
	@onlyIfMagRunning
	def script_toggleSmoothing(self, gesture):
		if self.checkSecureScreen():
			return
		val = toggleMagnifierKeyValue('UseBitmapSmoothing')
		if val:
			# Translators: The message reported when the user turns on smoothing.
			ui.message(_('Smoothing on'))
		else:
			# Translators: The message reported when the user turns off smoothing.
			ui.message(_('Smoothing off'))

	@script(
		description=DESC_TOGGLE_MOUSE_CURSOR_TRACKING_MODE,
	)
	@onlyIfMagRunning
	def script_toggleMouseCursorTrackingMode(self, gesture):
		if self.checkSecureScreen():
			return
		# Full screen tracking mode feature is available on Windows 10 build 17643 or higher.
		if not self.checkWindowsVersion(major=10, build=17643):
			# Translators: The message reported when the user tries to toggle mouse pointer tracking mode
			# whereas their Windows version does not support it.
			ui.message(_('Feature unavailable in this version of Windows.'))
			return
		# Feature applicable only to full screen view
		mode = getMagViewMode()
		if mode != MAG_VIEW_FULLSCREEN:
			# Translators: The message reported when the user tries to toggle mouse pointer tracking mode
			# while full screen view is not active.
			ui.message(_('Mouse pointer tracking mode applies only to full screen view.'))
			return
		val = toggleMagnifierKeyValue('FullScreenTrackingMode')
		if val:
			# Translators: A message reporting mouse pointer tracking mode (cf. option in Magnifier settings).
			ui.message(_('Centered on the screen'))
		else:
			# Translators: A message reporting mouse pointer tracking mode (cf. option in Magnifier settings).
			ui.message(_('Within the edge of the screen'))

	@script(
		description=DESC_TOGGLE_TEXT_CURSOR_TRACKING_MODE,
	)
	@onlyIfMagRunning
	def script_toggleTextCursorTrackingMode(self, gesture):
		if self.checkSecureScreen():
			return
		# Full screen tracking mode feature is available on Windows 10 build 18894 or higher.
		if not self.checkWindowsVersion(major=10, build=18894):
			# Translators: The message reported when the user tries to toggle text cursor tracking mode
			# whereas their Windows version does not support it.
			ui.message(_('Feature unavailable in this version of Windows.'))
			return
		# Feature applicable only to full screen view
		mode = getMagViewMode()
		if mode != MAG_VIEW_FULLSCREEN:
			# Translators: The message reported when the user tries to toggle text cursor tracking mode
			# while full screen view is not active.
			ui.message(_('Text cursor tracking mode applies only to full screen view.'))
			return
		val = toggleMagnifierKeyValue('CenterTextInsertionPoint')
		if val:
			# Translators: A message reporting text cursor tracking mode (cf. option in Magnifier settings).
			ui.message(_('Centered on the screen'))
		else:
			# Translators: A message reporting text cursor tracking mode (cf. option in Magnifier settings).
			ui.message(_('Within the edge of the screen'))

	@script(
		description=DESC_SAVE_MAGNIFIER_CONFIG,
	)
	def script_saveMagnifierConfig(self, gesture):
		if self.checkSecureScreen():
			return
		try:
			config.conf.disableProfileTriggers()
			for key, defaultValue in magnifierDefaultValuesMapping.items():
				config.conf['winMag']['magnifierConfig'][key] = getMagnifierKeyValue(key)
			ui.message(_("Magnifier config saved."))
		except Exception as e:
			log.error("Error saving Magnifier's config: {}".format(e), exc_info=True)
		finally:
			enableProfileTriggersAndActivate()
			config.conf.enableProfileTriggers()

	@script(
		description=DESC_RESTORE_MAGNIFIER_CONFIG,
	)
	def script_restoreMagnifierConfig(self, gesture):
		if self.checkSecureScreen():
			return
		try:
			config.conf.disableProfileTriggers()
			for key in magnifierDefaultValuesMapping.keys():
				val = config.conf['winMag']['magnifierConfig'][key]
				setMagnifierKeyValue(key, val)
			# Translators: A message reported when the user calls the command
			# to restores the Magnifier's configuration.
			ui.message(_("Magnifier config restored."))
		except Exception as e:
			log.error("Error while restoring magnifier's config: {}".format(e), exc_info=True)
		finally:
			enableProfileTriggersAndActivate()

	# This script has no description so that it cannot be mapped by the user to any gesture.
	# Indeed mapping a gesture to this script could cause it not to work if the mapped gesture
	# contains modifiers other than control and alt.
	@onlyIfMagRunning
	def script_moveViewLayeredCommand(self, gesture):
		try:
			mainKeyName = gesture.mainKeyName
		except AttributeError:
			# This gesture is not a KeyboardInputGesture, so mainKeyName attribut does not exist
			mainKeyName = None
		if mainKeyName and 'arrow' in mainKeyName.lower():
			self.report_viewMove(KeyboardInputGesture.fromName('control+alt+' + mainKeyName))
		else:
			log.error((
				"Only gestures containing arrow key may be mapped"
				" to script_moveViewLayeredCommand (gesture: {})."
			).format(gesture))
	script_moveViewLayeredCommand.allowMultipleLayeredCommands = True

	@script(
		description=DESC_MOVE_MOUSE_TO_VIEW,
	)
	@onlyIfMagRunning
	def script_moveMouseToView(self, gesture):
		mode = getMagViewMode()
		if mode == MAG_VIEW_FULLSCREEN:
			if Magnification.MagGetFullscreenTransform is None:
				# Translators: A message reported when the user tries to execute script mouseToView
				ui.message(_('Move mouse to view command available only on Windows 8 and above in full screen mode.'))
			elif isScreenCurtainActive():
				ui.message(
					# Translators: A message reported when the user tries to execute script mouseToView
					_('Move mouse to view command not available in full screen mode while screen curtain is active.')
				)
			return
		if mode == MAG_VIEW_DOCKED:
			# o = getDockedWindowObject()
			# hwnd = o.windowHandle
			# # Error on next line
			# rect = Magnification.MagGetWindowSource(hwnd)
			# Translators: A message reported when the user tries to execute script mouseToView
			ui.message(_('Move mouse to view not implemented for docked view'))
		view = View.getCurrentView(mode)
		x, y = view.centerPositionInScreen()
		winUser.setCursorPos(x, y)
		mouseHandler.executeMouseMoveEvent(x, y)

	@script(
		description=DESC_KEEP_MAG_WINDOW_ON_TOP,
	)
	@onlyIfMagRunning
	def script_keepMagWindowOnTop(self, gesture):
		if not config.isInstalledCopy():
			# Translators: A message reported when trying toggling "always on top" mode for Windows Magnifier's window
			# while running a portable NVDA.
			ui.message(_('Command only supported in installed versions of NVDA.'))
			return
		magHwnd = getMagnifierUIWindow()
		isOnTop = bool(winUser.user32.GetWindowLongW(magHwnd, winUser.GWL_EXSTYLE) & winUser.WS_EX_TOPMOST)
		if isOnTop != config.conf['winMag']['keepWindowAlwaysOnTop']:
			log.error(
				"Config synchronization error: "
				"isOnTop ({isOnTop}) != config.conf['winMag']['keepWindowAlwaysOnTop'] ({cfg})".format(
					isOnTop=isOnTop,
					cfg=config.conf['winMag']['keepWindowAlwaysOnTop'],
				)
			)
		onTop = not isOnTop
		if self.updateKeepMagWindowOnTop(onTop):
			config.conf['winMag']['keepWindowAlwaysOnTop'] = onTop
			if onTop:
				# Translators: A message reported when toggling "always on top" mode
				# for Windows Magnifier's control window
				msg = _("Magnifier controls always on top.")
			else:
				# Translators: A message reported when toggling "always on top" mode for Windows Magnifier's window
				msg = _("Magnifier controls not on top.")
			ui.message(msg)

	def updateKeepMagWindowOnTop(self, keepOnTop):
		if not config.isInstalledCopy():
			log.debug('This copy of NVDA is not installed; Update keep on top not processed.')
			return
		if not isMagnifierRunning():
			log.debug('Magnifier is not running; Update keep on top not processed.')
			return
		magHwnd = getMagnifierUIWindow()
		isOnTop = bool(winUser.user32.GetWindowLongW(magHwnd, winUser.GWL_EXSTYLE) & winUser.WS_EX_TOPMOST)
		if keepOnTop == isOnTop:
			# Nothing to do, the window state is already correct.
			return
		if keepOnTop:
			hWndInsertAfter = winUser2.HWND_TOPMOST
		else:
			hWndInsertAfter = winUser2.HWND_BOTTOM

		try:
			winUser2.setWindowPos(
				hWnd=magHwnd,
				hWndInsertAfter=hWndInsertAfter,
				X=0,
				Y=0,
				cx=0,
				cy=0,
				uFlags=winUser2.SWP_NOSIZE | winUser2.SWP_NOMOVE | winUser2.SWP_NOACTIVATE | winUser2.SWP_ASYNCWINDOWPOS,
			)
			return True
		except WindowsError as e:
			# Python 3 raises PermissionError which is a subclass of OSError alias WindowsError.
			# Python 2 raises WindowsError
			if e.winerror == 5:  # [WinError 5] Access is denied
				if config.isInstalledCopy():
					log.error('Unable to set window on topmost / not on top.')
				return False
			raise e

	def checkSecureScreen(self):
		if globalVars.appArgs.secure:
			# Translators: A message reported in secure screen when the user attempts to modify magnifiers settings.
			ui.message(_('Command unavailable on this screen.'))
		return globalVars.appArgs.secure

	def checkWindowsVersion(self, major, build):
		# Check current Windows version against a minimum required version passed as parameter.
		winVer = sys.getwindowsversion()
		return not (winVer.major < major or winVer.build < build)

	def getMagViewCenter(self):
		raise NotImplementedError  # zzz

	def modifyRunningState(self, gesture):
		val = _WaitForValueChangeForAction(
			gesture,
			fetcher=lambda: getMagnifierKeyValue('RunningState'),
			timeout=4,
		)
		if val == 1:
			# Translators: The message reported when the user turns on the Magnifier.
			ui.message(_('Magnifier on'))
		elif val == 0:
			# Translators: The message reported when the user turns off the Magnifier.
			ui.message(_('Magnifier off'))
		else:
			raise ValueError('Unexpected RunningState value: {}'.format(val))

	def modifyZoomLevel(self, gesture):
		if not config.conf['winMag']['reportZoom']:
			gesture.send()
			return
		val = _WaitForValueChangeForAction(
			gesture,
			fetcher=lambda: getMagnifierKeyValue('Magnification')
		)
		# Translators: A zoom level reported when the user changes the zoom level.
		ui.message(_('{zoomLevel}%'.format(zoomLevel=val)))

	def modifyColorInversion(self, gesture):
		val = _WaitForValueChangeForAction(
			gesture,
			fetcher=lambda: getMagnifierKeyValue('Invert'),
			timeout=0.5,
		)
		if val == 1:
			# Translators: The message reported when the user turns on color inversion.
			ui.message(_('Color inversion on'))
		elif val == 0:
			# Translators: The message reported when the user turns off color inversion.
			ui.message(_('Color inversion off'))
		else:
			raise ValueError('Unexpected Invert value: {}'.format(val))

	def modifyMagnificationView(self, gesture):
		fetcher = getMagViewMode
		val = _WaitForValueChangeForAction(gesture, fetcher)
		if val == MAG_VIEW_DOCKED:
			# Translators: A view type reported when the user changes the Magnifier view.
			# See the view menu items in the Magnifier's toolbar.
			ui.message(_('Docked'))
		elif val == MAG_VIEW_FULLSCREEN:
			# Translators: A view type reported when the user changes the Magnifier view.
			# See the view menu items in the Magnifier's toolbar.
			ui.message(_('Full screen'))
		elif val == MAG_VIEW_LENS:
			# Translators: A view type reported when the user changes the Magnifier view.
			# See the view menu items in the Magnifier's toolbar.
			ui.message(_('Lens'))
		else:
			raise ValueError('Unexpected MagnificationMode value: {}'.format(val))

	@script(
		description=DESC_OPEN_SETTINGS,
	)
	def script_openSettings(self, gesture):
		wx.CallAfter(
			gui.mainFrame._popupSettingsDialog,
			gui.settingsDialogs.NVDASettingsDialog,
			WinMagSettingsPanel,
		)

	@script(
		description=DESC_DISPLAY_HELP,
	)
	def script_displayHelp(self, gesture):
		# Translators: Title of the layered command help window.
		title = _("Windows Magnifier layered commands")
		cmdList = []
		for (gestures, command, desc) in self.__magLayerCommandList:
			cmdParts = []
			cmdParts.append(
				# Translators: Separator between key names in the layered command help window.
				_(', ').join(
					'+'.join(
						localizedKeyLabels.get(k.lower(), k) for k in gesture.split('+')
					) for gesture in gestures
				)
			)
			cmdParts.append(': ')
			cmdParts.append(desc)
			cmdList.append(''.join(cmdParts))
		cmdList = '\r'.join(cmdList)
		# Translators: Part of the help message displayed for the layered command help.
		msg = _("Magnifier layer commands:\n{cmdList}").format(cmdList=cmdList)
		ui.browseableMessage(msg, title)
