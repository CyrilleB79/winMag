# -*- coding: UTF-8 -*-
# globalPlugins/winMag/utils.py
# NVDA add-on: Windows Magnifier
# Copyright (C) 2019-2023 Cyrille Bougot
# This file is covered by the GNU General Public License.
# See the file COPYING.txt for more details.

from __future__ import unicode_literals

import winUser
from NVDAObjects.IAccessible import getNVDAObjectFromEvent
import vision
from visionEnhancementProviders.screenCurtain import ScreenCurtainProvider

try:
	import winreg
except ImportError:
	import _winreg as winreg


MAG_REGISTRY_KEY = r'Software\Microsoft\ScreenMagnifier'

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
	# 'RunningState': 0,
	'UseBitmapSmoothing': 1,
}


def getMagnifierKeyValue(name, useDefaultIfMissing=True):
	k = winreg.OpenKey(
		winreg.HKEY_CURRENT_USER,
		MAG_REGISTRY_KEY,
		0, winreg.KEY_READ | winreg.KEY_WOW64_64KEY
	)
	try:
		return winreg.QueryValueEx(k, name)[0]
	except WindowsError as e:
		if useDefaultIfMissing:
			return magnifierDefaultValuesMapping[name]
		raise e


def setMagnifierKeyValue(name, val):
	k = winreg.OpenKey(
		winreg.HKEY_CURRENT_USER,
		r'Software\Microsoft\ScreenMagnifier',
		0, winreg.KEY_READ | winreg.KEY_WRITE | winreg.KEY_WOW64_64KEY
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
	return getMagnifierUIWindow() != 0


def getDesktopChildObject(windowClassName):
	hWnd = winUser.user32.FindWindowW(windowClassName, 0)
	obj = getNVDAObjectFromEvent(hWnd, winUser.OBJID_CLIENT, 0)
	return obj if obj else None


def getMagnifierUIWindow():
	return winUser.user32.FindWindowW('MagUIClass', 0)


def getDockedWindowObject():
	return getDesktopChildObject(windowClassName="Screen Magnifier Window")


def getLensWindowObject():
	return getDesktopChildObject(windowClassName="Screen Magnifier Lens Window")


def isScreenCurtainActive():
	screenCurtainId = ScreenCurtainProvider.getSettings().getId()
	screenCurtainProviderInfo = vision.handler.getProviderInfo(screenCurtainId)
	isScreenCurtainRunning = bool(vision.handler.getProviderInstance(screenCurtainProviderInfo))
	return isScreenCurtainRunning
