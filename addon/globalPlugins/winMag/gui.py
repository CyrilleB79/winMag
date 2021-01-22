# -*- coding: UTF-8 -*-
# globalPlugins/winMag/gui.py
# NVDA add-on: Windows Magnifier
# Copyright (C) 2019-2021 Cyrille Bougot
#This file is covered by the GNU General Public License.
#See the file COPYING.txt for more details.

from __future__ import unicode_literals

from .msg import nvdaTranslation

import globalPluginHandler
import ui
import scriptHandler
import api
from tones import beep
from scriptHandler import script
from logHandler import log
import mouseHandler
import globalVars
import winUser

import wx

import sys


import addonHandler

addonHandler.initTranslation()

class WinMagPanel(gui.SettingsPanel):
	# Translators: This is the label for the Windows Magnifier settings panel.
	title = _("Windows Magnifier")
	
	feedbackLabels = (
		("off", zzz("off")),
		("speak", _("Speak")),
		("beep", _("Beep")),
	)

	def makeSettings(self, settingsSizer):
		sHelper = gui.guiHelper.BoxSizerHelper(self, sizer=settingsSizer)
		
		# Off / Vocal / Beeps
		self.reportMove = 
		# Translators: This is the label for a combobox in the
		# Windows Magnifier settings panel.
		reportMoveText = _("&")
		reportMoveChoices = [name for setting, name in self.reportMoveLabels]
				self.progressList=sHelper.addLabeledControl(progressLabelText, wx.Choice, choices=progressChoices)
				self.bindHelpEvent("ObjectPresentationProgressBarOutput", self.progressList)
				for index, (setting, name) in enumerate(self.progressLabels):
					if setting == config.conf["presentation"]["progressBarUpdates"]["progressBarOutputMode"]:
						self.progressList.SetSelection(index)
						break
				else:
					log.debugWarning("Could not set progress list to current report progress bar updates setting")
		
				
		
		# Off / Vocal / Beeps
		self.reportEdges = 
		
		self.reportZoomCheckBox = sHelper.addItem(
			# Translators: This is the label for a checkbox in the
			# Windows Magnifier settings panel.
			wx.CheckBox(self, label=_(""))
		)
		self.reportZoomCheckBox.SetValue(config.conf['winmag'][''])
		
		self.reportLensResizingCheckBox = sHelper.addItem(
			# Translators: This is the label for a checkbox in the
			# Windows Magnifier settings panel.
			wx.CheckBox(self, label=_(""))
		)
		self.reportLensResizingCheckBox.SetValue(config.conf['winmag'][''])
		# CB
		# Report toggle color inversion, select view
		self.reportOtherCheckBox = sHelper.addItem(
			# Translators: This is the label for a checkbox in the
			# Windows Magnifier settings panel.
			wx.CheckBox(self, label=_(""))
		)
		self.reportOtherCheckBox.SetValue(config.conf['winmag'][''])
		
		# When in documents, pass control+alt+arrow shortcut to magnifier:
		# Never, when not in table, always
		self.passCtrlAltArrow = 

	def onSave(self):
		zzz