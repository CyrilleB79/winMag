# -*- coding: UTF-8 -*-
# globalPlugins/winMag/gui.py
# NVDA add-on: Windows Magnifier
# Copyright (C) 2019-2021 Cyrille Bougot
#This file is covered by the GNU General Public License.
#See the file COPYING.txt for more details.

from __future__ import unicode_literals

from .msg import nvdaTranslation

import gui
import gui.guiHelper
import config
from logHandler import log

import wx

import addonHandler

addonHandler.initTranslation()


class WinMagSettingsPanel(gui.SettingsPanel):
	# Translators: This is the label for the Windows Magnifier settings panel.
	title = _("Windows Magnifier")
	
	reportMoveLabels = (
		("off", _("Off")),
		("speak", _("Speak")),
		("beep", _("Beep")),
	)
	passCtrlAltArrowLabels = (
		("never", _("Never")),
		("whenNotInTable", _("Only when not in table")),
		("always", _("Always")),
	)

	def makeSettings(self, settingsSizer):
		sHelper = gui.guiHelper.BoxSizerHelper(self, sizer=settingsSizer)
		
		# Translators: This is the label for a combobox in the
		# Windows Magnifier settings panel.
		reportMoveLabelText = _("Report view &moves:")
		reportMoveChoices = [name for setting, name in self.reportMoveLabels]
		self.reportMoveList = sHelper.addLabeledControl(reportMoveLabelText, wx.Choice, choices=reportMoveChoices)
		for index, (setting, name) in enumerate(self.reportMoveLabels):
			if setting == config.conf["winMag"]["reportMove"]:
				self.reportMoveList.SetSelection(index)
				break
		else:
			log.debugWarning("Could not set report move list to current setting")
		
		# Off / Vocal / Beeps
		#zzz self.reportEdges = 
		
		self.reportZoomCheckBox = sHelper.addItem(
			# Translators: This is the label for a checkbox in the
			# Windows Magnifier settings panel.
			wx.CheckBox(self, label=_("Report &zoom"))
		)
		self.reportZoomCheckBox.SetValue(config.conf['winMag']['reportZoom'])
		
		self.reportLensResizingCheckBox = sHelper.addItem(
			# Translators: This is the label for a checkbox in the
			# Windows Magnifier settings panel.
			wx.CheckBox(self, label=_("Report &lens resizing"))
		)
		self.reportLensResizingCheckBox.SetValue(config.conf['winMag']['reportLensResizing'])
		
		# Report toggle color inversion, select view
		self.reportOtherCheckBox = sHelper.addItem(
			# Translators: This is the label for a checkbox in the
			# Windows Magnifier settings panel.
			wx.CheckBox(self, label=_("Report &other commands"))
		)
		self.reportOtherCheckBox.SetValue(config.conf['winMag']['reportOther'])
		
		# Translators: This is the label for a combobox in the
		# Windows Magnifier settings panel.
		passCtrlAltArrowLabelText = _("In &documents, pass control+alt+arrows shortcuts to Windows Magnifier:")
		passCtrlAltArrowChoices = [name for setting, name in self.passCtrlAltArrowLabels]
		self.passCtrlAltArrowList = sHelper.addLabeledControl(passCtrlAltArrowLabelText, wx.Choice, choices=passCtrlAltArrowChoices)
		for index, (setting, name) in enumerate(self.passCtrlAltArrowLabels):
			if setting == config.conf["winMag"]["passCtrlAltArrow"]:
				self.passCtrlAltArrowList.SetSelection(index)
				break
		else:
			log.debugWarning("Could not set pass control alt arrow list to current setting")
	
	def onSave(self):
		config.conf["winMag"]["reportMove"] = self.reportMoveLabels[self.reportMoveList.GetSelection()][0]
		config.conf['winMag']['reportZoom'] = self.reportZoomCheckBox.IsChecked()
		config.conf['winMag']['reportLensResizing'] = self.reportLensResizingCheckBox.IsChecked()
		config.conf['winMag']['reportOther'] = self.reportOtherCheckBox.IsChecked()
		config.conf["winMag"]["passCtrlAltArrow"] = self.passCtrlAltArrowLabels[self.passCtrlAltArrowList.GetSelection()][0]
		