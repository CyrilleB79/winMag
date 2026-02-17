# -*- coding: UTF-8 -*-
# globalPlugins/winMag/utils.py
# NVDA add-on: Windows Magnifier
# Copyright (C) 2019-2026 Cyrille Bougot
# This file is covered by the GNU General Public License.
# See the file COPYING.txt for more details.

from __future__ import unicode_literals

import winUser
try:
	# NVDA version >= 2026.1
	from winBindings.user32 import FindWindow
# In Python 2, ModuleNotFoundError does not exist and the more general ImportError is raised instead.
except ImportError:
	# NVDA version < 2026.1
	from winUser import user32
	FindWindow = user32.FindWindowW
from NVDAObjects.IAccessible import getNVDAObjectFromEvent
try:
	# Python 3
	import winreg
except ImportError:
	# Python 2
	import _winreg as winreg


MAG_REGISTRY_KEY = r'Software\Microsoft\ScreenMagnifier'
COLOR_FILTERING_REGISTRY_KEY = r'SOFTWARE\Microsoft\ColorFiltering'

# Magnifier config mapping
magnifierDefaultValuesMapping = {
	'CenterTextInsertionPoint': 1,  # 0 = In screen edges, 1 = Centered
	'FollowCaret': 1,
	'FollowFocus': 1,
	'FollowMouse': 1,
	'FullScreenTrackingMode': 0,  # 0 = In screen edges, 1 = Centered
	'Invert': 0,
	'Magnification': 200,
	'MagnificationMode': 2,  # 2 = Full screen
	'RunningState': 0,
	'UseBitmapSmoothing': 1,
}

# Color filtering config mapping
colorFilteringDefaultValuesMapping = {
	'Active': 0,  # 0: Inactive, 1: Active
	'FilterType': 0,  # 0-5
	'HotkeyEnabled': 0,  # 0: Disabled, 1: Enabled
}

colorFilterNames = {
	# Translators: A color filter as listed in windows settings, Ease of Access, Color filters
	0: _("Grayscale"),
	# Translators: A color filter as listed in windows settings, Ease of Access, Color filters
	1: _("Inverted"),
	# Translators: A color filter as listed in windows settings, Ease of Access, Color filters
	2: _("Grayscale inverted"),
	# Translators: A color filter as listed in windows settings, Ease of Access, Color filters
	3: _("Red-green"),
	# Translators: A color filter as listed in windows settings, Ease of Access, Color filters
	4: _("Green-red"),
	# Translators: A color filter as listed in windows settings, Ease of Access, Color filters
	5: _("Blue-yellow"),
}

def getMagnifierKeyValue(name, useDefaultIfMissing=True):
	try:
		k = winreg.OpenKey(
			winreg.HKEY_CURRENT_USER,
			MAG_REGISTRY_KEY,
			0, winreg.KEY_READ | winreg.KEY_WOW64_64KEY,
		)
	except FileNotFoundError as e:
		if not useDefaultIfMissing:
			raise e
	else:
		try:
			return winreg.QueryValueEx(k, name)[0]
		except WindowsError as e:
			if not useDefaultIfMissing:
				raise e
	return magnifierDefaultValuesMapping[name]


def setMagnifierKeyValue(name, val):
	k = winreg.OpenKey(
		winreg.HKEY_CURRENT_USER,
		r'Software\Microsoft\ScreenMagnifier',
		0, winreg.KEY_READ | winreg.KEY_WRITE | winreg.KEY_WOW64_64KEY,
	)
	winreg.SetValueEx(k, name, 0, winreg.REG_DWORD, val)


def toggleMagnifierKeyValue(name):
	val = getMagnifierKeyValue(name)
	val = 0 if val == 1 else 1
	setMagnifierKeyValue(name, val)
	return val


def isMagnifierRunning():
	# We do not use the existing RunningState registry key because does not work in the following use case:
	# User logs off while Mag is active, then user logs on again. In this case,
	# even if Mag is not yet started by the user, the registry still holds RunningState value to 1.
	# Instead we use the Magnifier UI window that is always present, even if hidden.
	return bool(getMagnifierUIWindow())


def getColorFilteringKeyValue(name, useDefaultIfMissing=True):
	try:
		k = winreg.OpenKey(
			winreg.HKEY_CURRENT_USER,
			COLOR_FILTERING_REGISTRY_KEY,
			0, winreg.KEY_READ | winreg.KEY_WOW64_64KEY,
		)
	except FileNotFoundError as e:
		if not useDefaultIfMissing:
			raise e
	else:
		try:
			return winreg.QueryValueEx(k, name)[0]
		except WindowsError as e:
			if not useDefaultIfMissing:
				raise e
	return colorFilteringDefaultValuesMapping[name]


def getDesktopChildObject(windowClassName):
	hWnd = FindWindow(windowClassName, None)
	obj = getNVDAObjectFromEvent(hWnd, winUser.OBJID_CLIENT, 0)
	return obj if obj else None


def getMagnifierUIWindow():
	return FindWindow("MagUIClass", None)


def getDockedWindowObject():
	return getDesktopChildObject(windowClassName="Screen Magnifier Window")


def getLensWindowObject():
	return getDesktopChildObject(windowClassName="Screen Magnifier Lens Window")


def isScreenCurtainActive():
	try:
		# NVDA version >= 2026.1
		from screenCurtain import screenCurtain
		return screenCurtain is not None and screenCurtain.enabled
	# In Python 2, ModuleNotFoundError does not exist and the more general ImportError is raised instead.
	except ImportError:
		pass
	try:
		# For NVDA 2019.3+
		import vision
		from visionEnhancementProviders.screenCurtain import ScreenCurtainProvider
	# In Python 2, ModuleNotFoundError does not exist and the more general ImportError is raised instead.
	except ImportError:
		# For NVDA 2019.2.1 and below
		# No screen curtain feature
		return False
	screenCurtainId = ScreenCurtainProvider.getSettings().getId()
	screenCurtainProviderInfo = vision.handler.getProviderInfo(screenCurtainId)
	isScreenCurtainRunning = bool(vision.handler.getProviderInstance(screenCurtainProviderInfo))
	return isScreenCurtainRunning
