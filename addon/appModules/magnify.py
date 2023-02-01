# -*- coding: UTF-8 -*-
# appModules/magnify.py
# NVDA add-on: Windows Magnifier
# Copyright (C) 2023 Cyrille Bougot
# This file is covered by the GNU General Public License.
# See the file COPYING.txt for more details.

from appModuleHandler import AppModule
from scriptHandler import script
import globalPluginHandler
import NVDAObjects
import ui
from NVDAObjects import NVDAObject
from NVDAObjects.window import NVDAObject, Window
from NVDAObjects.IAccessible import IAccessible, List
from NVDAObjects.IAccessible import getNVDAObjectFromEvent
from NVDAObjects.behaviors import RowWithoutCellObjects, RowWithFakeNavigation
from NVDAObjects.UIA import UIA
from windowUtils import findDescendantWindow
import tones
import globalVars
import core
import config

from locationHelper import RectLTWH
import sys
import re
import threading

import addonHandler

addonHandler.initTranslation()

ADDON_SUMMARY = addonHandler.getCodeAddon ().manifest["summary"]


class AppModule(AppModule):
	
	scriptCategory = ADDON_SUMMARY
	
	def __init__(self,*args,**kwargs):
		super(AppModule,self).__init__(*args,**kwargs)
		
	def chooseNVDAObjectOverlayClasses(self, obj, clsList):
		super(AppModule, self).chooseNVDAObjectOverlayClasses(obj, clsList)
		if isinstance(obj, NVDAObjects.UIA.UIA) and obj.UIAAutomationId in ('ZoomInButton', 'ZoomOutButton'):
			clsList.insert(0, ZoomButton)


class ZoomButton(NVDAObjects.UIA.UIA):
	
	@script(
		gestures=['kb:space', 'kb:enter', 'kb:numpadEnter'],
	)
	def script_press(self, gesture):
		wmPlugin = next(p for p in globalPluginHandler.runningPlugins if 'winMag' in str(p))
		wmPlugin.modifyZoomLevel(gesture)
		
