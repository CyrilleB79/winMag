# -*- coding: UTF-8 -*-
#globalPlugins/winMag/__init__.py
#NVDA add-on: Windows Magnifier
#Copyright (C) 2019-2020 Cyrille Bougot
#This file is covered by the GNU General Public License.
#See the file COPYING.txt for more details.

from __future__ import unicode_literals

from .wmGui import WinMagSettingsPanel
from .msg import nvdaTranslation
from .magnification import Magnification 
from . import winUser2

import globalPluginHandler
import ui
import gui.settingsDialogs
import scriptHandler
import api
from tones import beep
from speech import speak
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
try:
	import winreg
except ImportError:
	import _winreg as winreg
import time
from functools import wraps
from types import MethodType

import addonHandler

addonHandler.initTranslation()

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
}
config.conf.spec["winMag"] = confspec


ADDON_SUMMARY = addonHandler.getCodeAddon ().manifest["summary"]

# Alpha-numeric keyboard Magnifier keys
# Translators: The key used natively byt the Magnifier on the alpha-numeric (main) keyboard in conjunction with Win key to zoom in.
KEY_ALPHA_PLUS = _("=")
# Translators: The key used natively byt the Magnifier on the alpha-numeric (main) keyboard in conjunction with Win key to zoom out.
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

MAG_REGISTRY_KEY = r'Software\Microsoft\ScreenMagnifier'

#Magnifier view types
MAG_VIEW_DOCKED = 1
MAG_VIEW_FULLSCREEN = 2
MAG_VIEW_LENS = 3

#Default config when names are not present in the key
MAG_DEFAULT_CENTER_TEXT_INSERTION_POINT = 1
MAG_DEFAULT_FOLLOW_CARET = 0
MAG_DEFAULT_FOLLOW_FOCUS = 0
MAG_DEFAULT_FOLLOW_MOUSE = 1
MAG_DEFAULT_FULL_SCREEN_TRACKING_MODE = 0
MAG_DEFAULT_INVERT = 1
MAG_DEFAULT_MAGNIFICATION = 200
MAG_DEFAULT_MAGNIFICATION_MODE = MAG_VIEW_FULLSCREEN
MAG_DEFAULT_RUNNING_STATE = 0
MAG_DEFAULT_USE_BITMAP_SMOOTHING = 1

def getMagnifierKeyValue(name, default=None):
	k = winreg.OpenKey(
		winreg.HKEY_CURRENT_USER,
		MAG_REGISTRY_KEY,
		0, winreg.KEY_READ | winreg.KEY_WOW64_64KEY
	)
	try:
		return winreg.QueryValueEx(k, name)[0]
	except WindowsError as e:
		if default is not None:
			return default
		raise e

def setMagnifierKeyValue(name, val):
	k = winreg.OpenKey(
		winreg.HKEY_CURRENT_USER,
		r'Software\Microsoft\ScreenMagnifier',
		0, winreg.KEY_READ | winreg.KEY_WRITE | winreg.KEY_WOW64_64KEY
	)
	winreg.SetValueEx(k, name, 0, winreg.REG_DWORD, val)
	
def toggleMagnifierKeyValue(name, default=None):
	val = getMagnifierKeyValue(name, default)
	val = 0 if val == 1 else 1
	setMagnifierKeyValue(name, val)
	return val
	
def isMagnifierRunning():
	# We do not use the existing RunningState registry key because does not work in the following use case:
	# User logs off while Mag is active, then user logs on again. Even if Mag is not yet started by the user, the registry still holds RunningState value to 1.
	# Instead we use the Magnifier UI window that is always present, even if hidden.
	return getMagnifierUIObject() is not None

def getDesktopChildObject(windowClassName):
	o = api.getDesktopObject().firstChild
	while o:
		if o.windowClassName == windowClassName:
			return o
		o = o.next
	return None

def getMagnifierUIObject():
	return getDesktopChildObject('MagUIClass') 

def getDockedWindowObject():
	return getDesktopChildObject(windowClassName="Screen Magnifier Window")

def isFullScreenView():
	return getMagnifierKeyValue('MagnificationMode', default=MAG_DEFAULT_MAGNIFICATION_MODE) == MAG_VIEW_FULLSCREEN

def isDockedOrFullScreenView():
	return getMagnifierKeyValue('MagnificationMode', default=MAG_DEFAULT_MAGNIFICATION_MODE) in [MAG_VIEW_DOCKED, MAG_VIEW_FULLSCREEN]

def onlyIfMagRunning(s):
	"""This script decorator allows the decorated script to execute only if the Magnifier is active.
	If not a message informs the user that the Magnifier is not running.
	"""
	
	@wraps(s)
	def script_wrapper(self, gesture):
		if not isMagnifierRunning():
			# Translators: The message reported when the user tries to use a Magnifier dedicated command while the Magnifier is not running.
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
		if not isDockedOrFullScreenView():
			# Translators: The message reported when the user tries to toggle a tracking mode while docked or full screen view is not active.
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

#Code taken from NVDA's source code NVDAObjects/window/winword.py
def _WaitForValueChangeForAction(gesture, fetcher, timeout=0.2, sleepTime=0.03):
	oldVal=fetcher()
	gesture.send()
	startTime=curTime=time.time()
	while (curTime-startTime)<timeout:
		curVal=fetcher()
		if curVal != oldVal:
			return curVal
		time.sleep(sleepTime)
		curTime=time.time()
	log.warning('No value change detected')
	return curVal

class NotInTableException(Exception):
	pass

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
		#This gesture is not a KeyboardInputGesture, so mainKeyName attribut does not exist
		mainKeyName = None
	if mainKeyName and mainKeyName.endswith('Arrow'):
		# Control+shift+arrows is caught by Magnifier when it is running to resize lens or docked windows.
		# Else it may correspond to another shortcut such as in Word where these gesture are the one to increase/decrease title level
		# or to move up/down a paragraph.
		if (
			config.conf['winMag']['reportLensResizing']
			and gesture.normalizedIdentifiers[0].split(':')[1] in ['alt+downarrow+shift', 'alt+leftarrow+shift', 'alt+rightarrow+shift', 'alt+shift+uparrow']
			and isMagnifierRunning()
		):
			winMagPlugin = [p for p in globalPluginHandler.runningPlugins if isinstance(p, GlobalPlugin)][0]
			return winMagPlugin.script_changeMagnificationWindowSize
		# For control+alt+arrow, create a compound script:
		# that will call Magnifier move commands (control+alt+arrow) rather than saying "Not in a table" message.
		if (
			config.conf['winMag']['passCtrlAltArrow'] != 'never'
			and gesture.normalizedIdentifiers[0].split(':')[1] in [
				'alt+control+downarrow',
				'alt+control+leftarrow',
				'alt+control+rightarrow',
				'alt+control+uparrow'
			]
			and isMagnifierRunning()
		):
			if oldScript:
				# We need a cache so that, for last script, checking wrapped script has always the same ref
				# else, getLastScriptRepeatCount would always return 0
				newScript = cached.get(oldScript, None)
				if not newScript:
					@wraps(oldScript)
					def newScript(self, g):
						global canRaiseNotInTableException
						if config.conf['winMag']['passCtrlAltArrow'] == 'always':
							executeMoveScript = True
						if config.conf['winMag']['passCtrlAltArrow'] == 'whenNotInTable':
							try:
								canRaiseNotInTableException = True
								oldScript(g)
								executeMoveScript = False
							except NotInTableException:
								executeMoveScript = True
							finally:
								canRaiseNotInTableException = False
						if executeMoveScript:
							winMagPlugin = [p for p in globalPluginHandler.runningPlugins if isinstance(p, GlobalPlugin)][0]
							winMagPlugin.script_moveView(g)
					try:
						newScript = MethodType(newScript, oldScript.__self__)
					except AttributeError:
					# oldScript.__self__ is not defined if oldScript is a function and not a bound method
					# This can happen in some addons' implementation of layered command
					# as well as the following definition in gestures.ini:
					# kb:a = kb:b
					# No patch in this case
						newScript = oldScript
					except:
					# If patching fails for any reason, log the error, but also return oldScript in order not to block NVDA.
						newScript = oldScript
						log.exception('Error patching script')
					cached = {oldScript: newScript}
				return newScript
			else:
				winMagPlugin = [p for p in globalPluginHandler.runningPlugins if isinstance(p, GlobalPlugin)][0]
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
	
	EVENTS_TRACKING_DEFAULT_VALUES = {
		'FollowCaret':  MAG_DEFAULT_FOLLOW_CARET,
		'FollowFocus':  MAG_DEFAULT_FOLLOW_FOCUS,
		'FollowMouse':  MAG_DEFAULT_FOLLOW_MOUSE,
		}
	lastTrackingConfig = None
	
	def __init__(self):
		pass
		
	def toggle(self, eventType):
		cfg = {n:getMagnifierKeyValue(n, d) for (n,d) in self.EVENTS_TRACKING_DEFAULT_VALUES.items()}
		if any(cfg.values()):
			self.__class__.lastTrackingConfig = dict(cfg)
		if eventType == 'All':
			if any(cfg.values()):
				cfg = {n:0 for n in cfg.keys()}
				val = 0
			else:
				lastCfg = self.__class__.lastTrackingConfig
				cfg = lastCfg if lastCfg is not None else {n:1 for n in cfg.keys()}
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

# Translators: The description for the toggleCaretTracking script.
DESC_TOGGLE_CARET_TRACKING = _("Toggles on or off caret tracking")
# Translators: The description for the toggleFocusTracking script.
DESC_TOGGLE_FOCUS_TRACKING = _("Toggles on or off focus tracking")
# Translators: The description for the toggleMouseTracking script.
DESC_TOGGLE_MOUSE_TRACKING = _("Toggles on or off mouse tracking")
# Translators: The description for the toggleTracking script.
DESC_TOGGLE_TRACKING = _("Toggles on or off tracking globally")
# Translators: The description for the toggleSmoothing script.
DESC_TOGGLE_SMOOTHING = _("Toggles on or off smoothing")
# Translators: The description for the toggleMouseCursorTrackingMode script.
DESC_TOGGLE_MOUSE_CURSOR_TRACKING_MODE = _("Switches between mouse tracking modes (within the edge of the screen or centered on the screen)")
# Translators: The description for the toggleTextCursorTrackingMode script.
DESC_TOGGLE_TEXT_CURSOR_TRACKING_MODE = _("Switches between text tracking modes (within the edge of the screen or centered on the screen)")
# Translators: The description for the moveView script.
DESC_MOVE_VIEW = _("Moves the magnified view")
# Translators: The description for the moveMouseToView script.
DESC_MOVE_MOUSE_TO_VIEW = _("Moves the mouse cursor in the center of the zoomed view")
# Translators: The description for the keepMagWindowOnTop script.
DESC_KEEP_MAG_WINDOW_ON_TOP = _("Switches on or off the mode keeping Windows Magnifier's window always on top of the other ones.")
# Translators: The description for the openSettings script.
DESC_OPEN_SETTINGS = _("Opens Windows Magnifier add-on settings")
# Translators: The description for the displayHelp script.
DESC_DISPLAY_HELP = _("Displays help on Magnifier layer commands")


class Screen:
	def __init__(self, width, height, minPos):
		self.width = width
		self.height = height
		self.minPos = minPos
		
	@classmethod
	def getCurrentScreen(cls):
		"""Create an instance from the current screen.
		"""
		if wx.Display.GetCount() != 1:
			# Translators: A message reported when the user tries to execute a script in multi-screen setup.
			ui.message(_('Multi-screen setup not yet supported. Please contact the add-on author to have it implemented.'))
			raise NotImplementedError('Multi-screen environment not yet implemented. Please contact add-on author.')
		displays = [wx.Display(i).GetGeometry() for i in range(wx.Display.GetCount())]
		width, height, minPos = mouseHandler.getTotalWidthAndHeightAndMinimumPosition(displays)
		return cls(width, height, minPos)
		

class View():
	def __init__(self, screen, zoomLevel, left, top):
		self.screen = screen
		self.zoomLevel = zoomLevel
		self.left = left
		self.top = top

	@property
	def width(self):
		return self.screen.width / self.zoomLevel
	
	@property
	def height(self):
		return self.screen.height / self.zoomLevel
		
	@property
	def center(self):
		minX, minY = self.screen.minPos
		# log.debug(f'minX={minX}; viewLeft={self.left}; screenWidth={self.screen.width}; viewWidth={self.width}')
		# log.debug(f'minY={minY}; viewTop={self.top}; screenHeight={self.screen.height}; viewHeight={self.height}')
		x = (self.left - minX) / (self.screen.width - self.width)
		y = (self.top - minY) / (self.screen.height - self.height)
		return x, y				

	@classmethod
	def getCurrentView(cls):
		screen = Screen.getCurrentScreen()
		try:
			Magnification.MagInitialize()
			zoomLevel, left, top = Magnification.MagGetFullscreenTransform()
		finally:
			Magnification.MagUninitialize()
		return cls(screen, zoomLevel, left, top)

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


class VolumeSlider(NVDAObjects.IAccessible.IAccessible):
	def event_valueChange(self,):
		pass

class GlobalPlugin(globalPluginHandler.GlobalPlugin):

	scriptCategory = ADDON_SUMMARY
	
	__magLayerScriptList = [
		(["c"], "toggleCaretTracking",DESC_TOGGLE_CARET_TRACKING),
		(["f"], "toggleFocusTracking",DESC_TOGGLE_FOCUS_TRACKING),
		(["m"], "toggleMouseTracking",DESC_TOGGLE_MOUSE_TRACKING),
		(["t"], "toggleTracking", DESC_TOGGLE_TRACKING),
		(["s"], "toggleSmoothing", DESC_TOGGLE_SMOOTHING),
		(["r"], "toggleMouseCursorTrackingMode", DESC_TOGGLE_MOUSE_CURSOR_TRACKING_MODE),
		(["x"], "toggleTextCursorTrackingMode", DESC_TOGGLE_TEXT_CURSOR_TRACKING_MODE),
		(["upArrow", "downArrow", "leftArrow", "rightArrow"], "moveViewLayeredCommand", DESC_MOVE_VIEW),
		(["v"], "moveMouseToView", DESC_MOVE_MOUSE_TO_VIEW),
		(["w"], "keepMagWindowOnTop", DESC_KEEP_MAG_WINDOW_ON_TOP),
		(["o"], "openSettings", DESC_OPEN_SETTINGS),
		(["h"], "displayHelp", DESC_DISPLAY_HELP),
	]
	
	
	def __init__(self):
		super(GlobalPlugin, self).__init__()
		gui.settingsDialogs.NVDASettingsDialog.categoryClasses.append(WinMagSettingsPanel)
		self.toggling = False
		ui.message = patched_message
		scriptHandler.findScript = patched_findScript 
		self.lastResize = None
		self.lastMoveDirection = None
		self.reportViewTimer = None
	
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
		description = _("Windows Magnifier layer commands entry point."),
		gesture = "kb:NVDA+windows+O"
	)
	@onlyIfMagRunning
	def script_magLayer(self, gesture):
		# A run-time binding will occur from which we can perform various layered commands.
		# First, check if a second press of the script was done.
		if self.toggling:
			self.script_error(gesture)
			return
		layerGestures = {}
		for (keys, script, desc) in self.__magLayerScriptList:
			for key in keys:
				layerGestures["kb:" + key] = script
		self.bindGestures(layerGestures)
		self.toggling = True
		beep(100, 10)

	def terminate(self):
		ui.message = orig_message
		scriptHandler.findScript = orig_findScript 
		self.toggleKeepMagWindowOnTop(keepOnTop=True, reportMessage=False)  # Restore to default behaviour.
		gui.settingsDialogs.NVDASettingsDialog.categoryClasses.remove(WinMagSettingsPanel)
		super().terminate()
	
	@script(
		gestures = ["kb:windows+numpadPlus", "kb:windows+numLock+numpadPlus", "kb:windows+" + KEY_ALPHA_PLUS, "kb:windows+plus"]
		)	
	def script_zoomIn(self, gesture):
		numlockWasOn = 'numlock' in gesture.normalizedIdentifiers[0].split(':')[1]
		if config.conf['winMag']['reportZoom'] and isMagnifierRunning():
			self.modifyZoomLevel(gesture)
		elif config.conf['winMag']['reportTurnOnOff'] and not isMagnifierRunning():
			self.modifyRunningState(gesture)
		else:
			gesture.send()
		if numlockWasOn:
			# A gesture.send() with numlock on will unwantedly toggle numlock (see NVDA issue #10827), so restore it.
			KeyboardInputGesture.fromName('numlock').send()
		
	
	@script(
		gestures = ["kb:windows+numpadMinus", "kb:windows+numLock+numpadMinus", "kb:windows+" + KEY_ALPHA_MINUS, "kb:windows+-"]
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
		gesture = "kb:windows+escape"
	)
	def script_quitMagnifier(self, gesture):
		if config.conf['winMag']['reportTurnOnOff'] and isMagnifierRunning():
			self.modifyRunningState(gesture)
		else:
			gesture.send()
		
	@script(
		gesture = "kb:control+alt+I"
	)
	def script_toggleColorInversion(self, gesture):
		if config.conf['winMag']['reportColorInversion'] and isMagnifierRunning():
			self.modifyColorInversion(gesture)
		else:
			gesture.send()
	
	@script(
		gestures = ["kb:control+alt+M", "kb:control+alt+D", "kb:control+alt+F", "kb:control+alt+L"]
	)
	def script_changeMagnificationView(self, gesture):
		if config.conf['winMag']['reportViewChange'] and isMagnifierRunning():
			self.modifyMagnificationView(gesture)
		else:
			gesture.send()
	
	def script_moveView(self, gesture):
		self.report_viewMove(gesture)
		
	def report_viewMove(self, gesture):
		gesture.send()
		reportMoves = config.conf['winMag']['reportViewMove'] != 'off'
		reportEdges = config.conf['winMag']['reportMoveToScreenEdges'] != 'off'
		if not (reportMoves or reportEdges) and not isFullScreenView():
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
		
		view = View.getCurrentView()
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
			self.reportViewTimer = wx.CallLater(300, lambda: self.report_viewPosition(direction))
		
	def reportScreenEdge(self):
		if config.conf['winMag']['reportMoveToScreenEdges'] == 'speech':
			# Translators: A message reported when the user reaches the edge of the screen while moving the view.
			ui.message(_('Edge of the screen.'))
		elif config.conf['winMag']['reportMoveToScreenEdges'] == 'tones':
			# Compute the pitch for the note 2 tones above max coordinate pitch.
			edgePitch = config.conf['mouse']['audioCoordinates_maxPitch']*2**(4/12)
			vol = config.conf['winMag']['toneVolume']
			beep(edgePitch, 30, vol, vol)
			time.sleep(0.06)
			beep(edgePitch, 30, vol, vol)
		else:
			raise RuntimeError('Unexpected config {config}'.format(config=config.conf['winMag']['reportViewMove']))
	
	def report_viewPosition(self, direction, view=None):
		if view is None:
			view = View.getCurrentView()
		
		if view.zoomLevel == 1:
			return
		x, y = view.center
		if direction == 'horizontal':
			val = x
		elif 	direction == 'vertical':
			val = y
		if config.conf['winMag']['reportViewMove'] == 'speech':
			precision = 0 if view.zoomLevel < 4 else 1
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
			mode = getMagnifierKeyValue('MagnificationMode', default=MAG_DEFAULT_MAGNIFICATION_MODE)
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
				# Translators: A message reported when the user uses resizing shortcuts (control+shift+arrow) in full screen view.
				ui.message(_('Resizing not available in full screen.'))
		else:
			raise RuntimeError('Unexpected case')
		
	@script(
		description = DESC_TOGGLE_CARET_TRACKING
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
		description = DESC_TOGGLE_FOCUS_TRACKING
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
		description = DESC_TOGGLE_MOUSE_TRACKING
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
		description = DESC_TOGGLE_TRACKING,
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
			ui.message(_('Tracking on'))
		else:
			# Translators: The message reported when the user turns off tracking.
			ui.message(_('Tracking off'))
	
	@script(
		description = DESC_TOGGLE_SMOOTHING
	)
	@onlyIfMagRunning
	def script_toggleSmoothing(self, gesture):
		if self.checkSecureScreen():
			return
		val = toggleMagnifierKeyValue('UseBitmapSmoothing', default=MAG_DEFAULT_USE_BITMAP_SMOOTHING)
		if val:
			# Translators: The message reported when the user turns on smoothing.
			ui.message(_('Smoothing on'))
		else:
			# Translators: The message reported when the user turns off smoothing.
			ui.message(_('Smoothing off'))
	
	@script(
		description = DESC_TOGGLE_MOUSE_CURSOR_TRACKING_MODE
	)
	@onlyIfMagRunning
	def script_toggleMouseCursorTrackingMode(self, gesture):
		if self.checkSecureScreen():
			return
		# Full screen tracking mode feature is available on Windows 10 build 17643 or higher.
		if not self.checkWindowsVersion(major=10, build=17643):
			# Translators: The message reported when the user tries to toggle mouse tracking mode whereas his Windows version does not support it.
			ui.message(_('Feature unavailable in this version of Windows.'))
			return
		# Feature applicable only to full screen view
		if not isFullScreenView():
			# Translators: The message reported when the user tries to toggle mouse tracking mode while full screen view is not active.
			ui.message(_('Mouse tracking mode applies only to full screen view.'))
			return
		val = toggleMagnifierKeyValue('FullScreenTrackingMode', default=MAG_DEFAULT_FULL_SCREEN_TRACKING_MODE)
		if val:
			# Translators: A message reporting mouse cursor tracking mode (cf. option in Magnifier settings).
			ui.message(_('Centered on the screen'))
		else:
			# Translators: A message reporting mouse cursor tracking mode (cf. option in Magnifier settings).
			ui.message(_('Within the edge of the screen'))

	@script(
		description = DESC_TOGGLE_TEXT_CURSOR_TRACKING_MODE
	)
	@onlyIfMagRunning
	def script_toggleTextCursorTrackingMode(self, gesture):
		if self.checkSecureScreen():
			return
		# Full screen tracking mode feature is available on Windows 10 build 18894 or higher.
		if not self.checkWindowsVersion(major=10, build=18894):
			# Translators: The message reported when the user tries to toggle mouse tracking mode whereas his Windows version does not support it.
			ui.message(_('Feature unavailable in this version of Windows.'))
			return
		# Feature applicable only to full screen view
		if not isFullScreenView():
			# Translators: The message reported when the user tries to toggle mouse tracking mode while full screen view is not active.
			ui.message(_('Mouse tracking mode applies only to full screen view.'))
			return
		val = toggleMagnifierKeyValue('CenterTextInsertionPoint', default=MAG_DEFAULT_CENTER_TEXT_INSERTION_POINT)
		if val:
			# Translators: A message reporting mouse cursor tracking mode (cf. option in Magnifier settings).
			ui.message(_('Centered on the screen'))
		else:
			# Translators: A message reporting mouse cursor tracking mode (cf. option in Magnifier settings).
			ui.message(_('Within the edge of the screen'))

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
			# Translators: A message reported when the user tries to execute script moveView.
			ui.message(_("Only gestures containing arrow key may be mapped to this script."))
	script_moveViewLayeredCommand.allowMultipleLayeredCommands = True
	
	@script(
		description = DESC_MOVE_MOUSE_TO_VIEW
	)
	@onlyIfMagRunning
	def script_moveMouseToView(self, gesture):
		if Magnification.MagGetFullscreenTransform is None:
			# Translators: A message reported when the user tries to execute script mouseToView
			ui.message(_('Move mouse to view command available only on Windows 8 and above.'))
			return
		mode = getMagnifierKeyValue('MagnificationMode', default=MAG_DEFAULT_MAGNIFICATION_MODE)
		if mode == MAG_VIEW_LENS:
			# Translators: A message reported when the user tries to execute script mouseToView
			ui.message(_('Move mouse to view not applicable with lense view.'))
			return
		Magnification.MagInitialize()
		try:
			if mode == MAG_VIEW_FULLSCREEN:
				zoomLevel, viewLeft, viewTop = Magnification.MagGetFullscreenTransform()
			elif mode == MAG_VIEW_DOCKED:
				# o = getDockedWindowObject()
				# hwnd = o.windowHandle
				# # Error on next line
				# rect = Magnification.MagGetWindowSource(hwnd)
				# Translators: A message reported when the user tries to execute script mouseToView
				ui.message(_('Move mouse to view not implemented for docked view'))
		finally:
			Magnification.MagUninitialize()
		if wx.Display.GetCount() != 1:
			# Translators: A message reported when the user tries to execute script mouseToView
			ui.message(_('This command is not yet available in multi-screen environment. Please contact the add-on author to have it implemented.'))
			return
		rect = wx.Display(0).GetGeometry()
		viewHeight = rect.height / zoomLevel
		viewWidth = rect.width / zoomLevel
		x = viewLeft + int(viewWidth/2)
		y = viewTop + int(viewHeight/2)
		winUser.setCursorPos(x,y)
		mouseHandler.executeMouseMoveEvent(x,y)
	
	@script(
		description = DESC_KEEP_MAG_WINDOW_ON_TOP,
	)
	@onlyIfMagRunning
	def script_keepMagWindowOnTop(self, gesture):
		self.toggleKeepMagWindowOnTop()
	
	def toggleKeepMagWindowOnTop(self, keepOnTop=None, reportMessage=True):
	
		magHwnd = getMagnifierUIObject().windowHandle
		
		if keepOnTop is None:
			# Toggle current value.
			keepOnTop = not bool(winUser.user32.GetWindowLongW(magHwnd, winUser.GWL_EXSTYLE) & winUser.WS_EX_TOPMOST)
		
		if keepOnTop:
			hWndInsertAfter = winUser2.HWND_TOPMOST
			# Translators: A message reported when toggling "always on top" mode for Windows Magnifier's window
			msg = _("Window always on top.")
		else:
			hWndInsertAfter = winUser2.HWND_BOTTOM
			# Translators: A message reported when toggling "always on top" mode for Windows Magnifier's window
			msg = _("Window not on top.")
		
		winUser2.setWindowPos(
			hWnd=magHwnd, 
			hWndInsertAfter=hWndInsertAfter,
			X=0,
			Y=0,
			cx=0,
			cy=0,
			uFlags=winUser2.SWP_NOSIZE | winUser2.SWP_NOMOVE | winUser2.SWP_NOACTIVATE | winUser2.SWP_ASYNCWINDOWPOS,
		)
		if reportMessage:
			ui.message(msg)	

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
		zzz

	def modifyRunningState(self, gesture):
		fetcher = lambda: getMagnifierKeyValue('RunningState', default=MAG_DEFAULT_RUNNING_STATE)
		val = _WaitForValueChangeForAction(gesture, fetcher, timeout=4)
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
		fetcher = lambda: getMagnifierKeyValue('Magnification', default=MAG_DEFAULT_MAGNIFICATION)
		val = _WaitForValueChangeForAction(gesture, fetcher)
		# Translators: A zoom level reported when the user changes the zoom level.
		ui.message(_('{zoomLevel}%'.format(zoomLevel=val)))
		
	def modifyColorInversion(self, gesture):
		fetcher = lambda: getMagnifierKeyValue('Invert', default=MAG_DEFAULT_INVERT)
		val = _WaitForValueChangeForAction(gesture, fetcher, timeout=0.5)
		if val == 1:
			# Translators: The message reported when the user turns on color inversion.
			ui.message(_('Color inversion on'))
		elif val == 0:
			# Translators: The message reported when the user turns off color inversion.
			ui.message(_('Color inversion off'))
		else:
			raise ValueError('Unexpected Invert value: {}'.format(val))
			
	def modifyMagnificationView(self, gesture):
		fetcher = lambda: getMagnifierKeyValue('MagnificationMode', default=MAG_DEFAULT_MAGNIFICATION_MODE)
		val = _WaitForValueChangeForAction(gesture, fetcher)
		if val == MAG_VIEW_DOCKED:
			# Translators: A view type reported when the user changes the Magnifier view. See the view menu items in the Magnifier's toolbar.
			ui.message(_('Docked'))
		elif val == MAG_VIEW_FULLSCREEN:
			# Translators: A view type reported when the user changes the Magnifier view. See the view menu items in the Magnifier's toolbar.
			ui.message(_('Full screen'))
		elif val == MAG_VIEW_LENS:
			# Translators: A view type reported when the user changes the Magnifier view. See the view menu items in the Magnifier's toolbar.
			ui.message(_('Lens'))
		else:
			raise ValueError('Unexpected MagnificationMode value: {}'.format(val))

	@script(
		description = DESC_OPEN_SETTINGS,
	)
	def script_openSettings(self, gesture):
		wx.CallAfter(gui.mainFrame._popupSettingsDialog, gui.settingsDialogs.NVDASettingsDialog, WinMagSettingsPanel)

	@script(
		description = DESC_DISPLAY_HELP
	)
	def script_displayHelp(self, gesture):
		# Translators: Title of the layered command help window.
		title = _("Windows Magnifier layered commands")
		cmdList = []
		for (keys, script, desc) in self.__magLayerScriptList:
			cmdList.append(
				# Translators: Separator between key names in the layered command help window.
				_(', ').join(localizedKeyLabels.get(k.lower(), k) for k in keys)
				+ ': ' + desc
			)
		cmdList = '\r'.join(cmdList)
		# Translators: Part of the help message displayed for the layered command help.
		msg = _("Magnifier layer commands:\n{cmdList}").format(cmdList=cmdList)
		ui.browseableMessage(msg, title)
