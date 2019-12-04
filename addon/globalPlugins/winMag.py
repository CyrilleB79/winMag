# -*- coding: UTF-8 -*-
#globalPlugins/winMag.py
#NVDA add-on: Windows Magnifier
#Copyright (C) 2019 Cyrille Bougot
#This file is covered by the GNU General Public License.
#See the file COPYING.txt for more details.

from __future__ import unicode_literals

import globalPluginHandler
import ui
from tones import beep
from scriptHandler import script
from logHandler import log

import sys
try:
	import winreg
except ImportError:
	import _winreg as winreg
import time
from functools import wraps

import addonHandler

addonHandler.initTranslation()

ADDON_SUMMARY = addonHandler.getCodeAddon ().manifest["summary"]

MAG_REGISTRY_KEY = r'Software\Microsoft\ScreenMagnifier'

#Magnifier view types
MAG_VIEW_DOCKED = 1
MAG_VIEW_FULLSCREEN = 2
MAG_VIEW_LENS = 3

#Default config when names are not present in the key
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
	return getMagnifierKeyValue('RunningState', default=MAG_DEFAULT_RUNNING_STATE)

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
			# Translators: The message reported when the user tries to use a Magnifier dedicated command while the Magnifier is not running
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
			ui.message(_('Tracking configuration only applicable to docked or full screen view.'))
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
def _WaitForValueChangeForAction(gesture, fetcher, timeout=0.2):
	oldVal=fetcher()
	gesture.send()
	startTime=curTime=time.time()
	while (curTime-startTime)<timeout:
		curVal=fetcher()
		if curVal != oldVal:
			return curVal
		time.sleep(0.03)
		curTime=time.time()
	log.warning('No value change detected')
	return curVal

class TrackingConfig(object):
	
	DEFAULT_TRACKING_CONFIG = {
		'FollowCaret':  MAG_DEFAULT_FOLLOW_CARET,
		'FollowFocus':  MAG_DEFAULT_FOLLOW_FOCUS,
		'FollowMouse':  MAG_DEFAULT_FOLLOW_MOUSE,
		}
	lastTrackingConfig = None
	
	def __init__(self):
		pass
		
	def toggle(self, eventType):
		cfg = {n:getMagnifierKeyValue(n, d) for (n,d) in self.DEFAULT_TRACKING_CONFIG.items()}
		if any(cfg.values()):
			self.__class__.lastTrackingConfig = dict(cfg)
		if eventType == 'All':
			if any(cfg.values()):
				cfg = {n:0 for n in cfg.keys()}
				val = 0
			else:
				cfg = self.__class__.lastTrackingConfig 
				if cfg is None:
					cfg = self.DEFAULT_TRACKING_CONFIG
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

class GlobalPlugin(globalPluginHandler.GlobalPlugin):

	scriptCategory = ADDON_SUMMARY
	
	def __init__(self):
		super(GlobalPlugin, self).__init__()
		self.toggling = False
		
	def getScript(self, gesture):
		if not self.toggling:
			return globalPluginHandler.GlobalPlugin.getScript(self, gesture)
		script = globalPluginHandler.GlobalPlugin.getScript(self, gesture)
		if not script:
			script = finally_(self.script_error, self.finish)
		return finally_(script, self.finish)

	def finish(self):
		self.toggling = False
		self.clearGestureBindings()
		self.bindGestures(self.__gestures)

	def script_error(self, gesture):
		beep(120, 100)

	@script(
		# Translators: The description for the layered command script basis
		description = _("Magnifier layer commands: C: Toggle caret tracking, F: Toggle focus tracking, M: Toggle mouse tracking, T: toggle tracking, S: Toggle smoothing, R: Toggle mouse tracking mode, H: Help on layered commands."),
		gesture = "kb:NVDA+windows+M"
	)
	@onlyIfMagRunning
	def script_magLayer(self, gesture):
		# A run-time binding will occur from which we can perform various layered commands.
		# First, check if a second press of the script was done.
		if self.toggling:
			self.script_error(gesture)
			return
		self.bindGestures(self.__magLayerGestures)
		self.toggling = True
		beep(100, 10)

	def terminate(self):
		pass
	
	@script(
		gestures = ["kb:windows+numpadPlus", "kb:windows+numLock+numpadPlus", "kb:windows+="]
		)	
	def script_zoomIn(self, gesture):
		if isMagnifierRunning():
			self.modifyZoomLevel(gesture)
		else:
			self.modifyRunningState(gesture)
	
	@script(
		gestures = ["kb:windows+-", "kb:windows+numpadMinus", "kb:windows+numLock+numpadMinu"]
	)	
	def script_zoomOut(self, gesture):
		if isMagnifierRunning():
			self.modifyZoomLevel(gesture)
		else:
			gesture.send()
		
	@script(
		gesture = "kb:windows+escape"
	)
	def script_quitMagnifier(self, gesture):
		if isMagnifierRunning():
			self.modifyRunningState(gesture)
		else:
			gesture.send()
		
	@script(
		gesture = "kb:control+alt+I"
	)
	def script_toggleColorInversion(self, gesture):
		if isMagnifierRunning():
			self.modifyColorInversion(gesture)
		else:
			gesture.send()
	
	@script(
		gestures = ["kb:control+alt+M", "kb:control+alt+D", "kb:control+alt+F", "kb:control+alt+L"])
	def script_changeMagnificationView(self, gesture):
		if isMagnifierRunning():
			self.modifyMagnificationView(gesture)
		else:
			gesture.send()

	@script(
		# Translators: The description for the toggleCaretTracking script
		description = _("Toggle caret tracking"),
	)
	@onlyIfMagRunning
	@onlyIfDockedOrFullScreenView
	def script_toggleCaretTracking(self, gesture):
		cfg = TrackingConfig()
		val = cfg.toggle('FollowCaret')
		if val:
			# Translators: The message reported when the user turns on caret tracking
			ui.message(_('Caret tracking on'))
		else:
			# Translators: The message reported when the user turns off caret tracking
			ui.message(_('Caret tracking off'))
	
	@script(
		# Translators: The description for the toggleFocusTracking script
		description = _("Toggle focus tracking"),
	)
	@onlyIfMagRunning
	@onlyIfDockedOrFullScreenView
	def script_toggleFocusTracking(self, gesture):
		cfg = TrackingConfig()
		val = cfg.toggle('FollowFocus')
		if val:
			# Translators: The message reported when the user turns on focus tracking
			ui.message(_('Focus tracking on'))
		else:
			# Translators: The message reported when the user turns off focus tracking
			ui.message(_('Focus tracking off'))

	@script(
		# Translators: The description for the toggleMouseTracking script
		description = _("Toggle mouse tracking"),
	)
	@onlyIfMagRunning
	@onlyIfDockedOrFullScreenView
	def script_toggleMouseTracking(self, gesture):
		cfg = TrackingConfig()
		val = cfg.toggle('FollowMouse')
		if val:
			# Translators: The message reported when the user turns on mouse tracking
			ui.message(_('Mouse tracking on'))
		else:
			# Translators: The message reported when the user turns off focus tracking
			ui.message(_('Mouse tracking off'))
	@script(
		# Translators: The description for the toggleTracking script
		description = _("Toggle tracking"),
	)
	@onlyIfMagRunning
	@onlyIfDockedOrFullScreenView
	def script_toggleTracking(self, gesture):
		cfg = TrackingConfig()
		val = cfg.toggle('All')
		if val:
			# Translators: The message reported when the user turns on tracking
			ui.message(_('Tracking on'))
		else:
			# Translators: The message reported when the user turns off tracking
			ui.message(_('Tracking off'))
	
	@script(
		# Translators: The description for the toggleSmoothing script
		description = _("Toggle smoothing"),
	)
	@onlyIfMagRunning
	def script_toggleSmoothing(self, gesture):
		val = toggleMagnifierKeyValue('UseBitmapSmoothing', default=MAG_DEFAULT_USE_BITMAP_SMOOTHING)
		if val:
			# Translators: The message reported when the user turns on smoothing
			ui.message(_('Smoothing on'))
		else:
			# Translators: The message reported when the user turns off smoothing
			ui.message(_('Smoothing off'))
	
	@script(
		# Translators: The description for the toggleMouseCursorTrackingMode script
		description = _("Toggle mouse tracking mode"),
	)
	@onlyIfMagRunning
	def script_toggleMouseCursorTrackingMode(self, gesture):
		# Feature available on Windows 10 build 17643 or higher.
		winVer = sys.getwindowsversion()
		if  winVer.major < 10 or winVer.build < 17643:
			# Translators: The message reported when the user tries to toggle mouse tracking mode whereas his OS version does not support it.
			ui.message(_('Feature unavailable on this OS version.'))
			return
		if not isFullScreenView():
			# Translators: The message reported when the user tries to toggle mouse tracking mode while full screen view is not active.
			ui.message(_('Mouse tracking mode applies only to full screen view.'))
			return
		val = toggleMagnifierKeyValue('FullScreenTrackingMode', default=MAG_DEFAULT_FULL_SCREEN_TRACKING_MODE)
		if val:
			# Translators: A message reporting mouse cursor tracking mode (cf. option in Magnifier settings)
			ui.message(_('Centered on the screen'))
		else:
			# Translators: A message reporting mouse cursor tracking mode (cf. option in Magnifier settings)
			ui.message(_('Within the edge of the screen'))

	def modifyRunningState(self, gesture):
		fetcher = lambda: getMagnifierKeyValue('RunningState', default=MAG_DEFAULT_RUNNING_STATE)
		val = _WaitForValueChangeForAction(gesture, fetcher, timeout=2)
		if val == 1:
			# Translators: The message reported when the user turns on the Magnifier
			ui.message(_('Magnifier on'))
		elif val == 0:
			# Translators: The message reported when the user turns off the Magnifier
			ui.message(_('Magnifier off'))
		else:
			raise ValueError('Unexpected RunningState value: {}'.format(val))
			
	def modifyZoomLevel(self, gesture):
		fetcher = lambda: getMagnifierKeyValue('Magnification', default=MAG_DEFAULT_MAGNIFICATION)
		val = _WaitForValueChangeForAction(gesture, fetcher)
		# Translators: A zoom level reported when the user changes the zoom level
		ui.message(_('{}%'.format(val)))
		
	def modifyColorInversion(self, gesture):
		fetcher = lambda: getMagnifierKeyValue('Invert', default=MAG_DEFAULT_INVERT)
		val = _WaitForValueChangeForAction(gesture, fetcher, timeout=0.5)
		if val == 1:
			# Translators: The message reported when the user turns on color inversion
			ui.message(_('Color inversion on'))
		elif val == 0:
			# Translators: The message reported when the user turns off color inversion
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

	def script_displayHelp(self, gesture):
		# Translators: The help message reported for the layered command help.
		msg = _("Magnifier layer commands: C: Toggle caret tracking, F: Toggle focus tracking, M: Toggle mouse tracking, T: toggle tracking, S: Toggle smoothing, R: Toggle mouse tracking mode, H: Help on layered commands.")
		ui.message(msg)
		
	__magLayerGestures = {
		"kb:c": "toggleCaretTracking",
		"kb:f": "toggleFocusTracking",
		"kb:m": "toggleMouseTracking",
		"kb:t": "toggleTracking",
		"kb:s": "toggleSmoothing",
		"kb:r": "toggleMouseCursorTrackingMode",
		"kb:h": "displayHelp",
	}
