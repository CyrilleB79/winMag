# -*- coding: UTF-8 -*-
#gui.py
#NVDA add-on: Windows Magnifier
#Copyright (C) 2019-2020 Cyrille Bougot
#This file is covered by the GNU General Public License.
#See the file COPYING.txt for more details.

from .wmconfig import moveViewReportOptions

import gui
import globalVars
import config
import addonHandler

import wx

addonHandler.initTranslation()

class WinMagSettingsPanel(gui.SettingsPanel):
	# Translators: This is the label for the Windows Magnifier add-on settings panel.
	title = _("Windows Magnifier")
	
	def makeSettings(self, settingsSizer):
		sHelper = gui.guiHelper.BoxSizerHelper(self, sizer=settingsSizer)
		
		# Translators: This is the label for a combobox in the
		# Windows Magnifier settings panel.
		viewMoveLabelText = _("Report view moves:")
		self.viewMoveValues = [x[0] for x in moveViewReportOptions]
		viewMoveChoices = [x[1] for x in moveViewReportOptions]
		self.viewMoveComboBox = sHelper.addLabeledControl(viewMoveLabelText, wx.Choice, choices=viewMoveChoices)
		try:
			index = self.viewMoveValues.index(config.conf["winmag"]["reportViewMoves"])
		except ValueError:
			index = 0
		self.viewMoveComboBox.SetSelection(index)
		
		# Translators: This is the label for a checkbox in the
		# Windows Magnifier settings panel.
		viewResizingText = _("Report the resizing of the view (docked and lense only)")
		self.viewResizingCheckBox = wx.CheckBox(self, label=viewResizingText)
		self.viewResizingCheckBox.SetValue(config.conf["winmag"]["reportViewResizing"])
		sHelper.addItem(self.viewResizingCheckBox)

	def onSave(self):
		config.conf["winmag"]["reportViewMoves"] = self.viewMoveValues[self.viewMoveComboBox.GetSelection()]
		config.conf["winmag"]["reportViewResizing"] = self.viewResizingCheckBox.IsChecked()

