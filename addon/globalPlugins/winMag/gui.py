# -*- coding: UTF-8 -*-
#gui.py
#NVDA add-on: Windows Magnifier
#Copyright (C) 2019-2020 Cyrille Bougot
#This file is covered by the GNU General Public License.
#See the file COPYING.txt for more details.

import wx
import gui
import globalVars
import config
import addonHandler

addonHandler.initTranslation()

class WinMagSettingsPanel(gui.SettingsPanel):
	# Translators: This is the label for the Windows Magnifier add-on settings panel.
	title = _("Windows Magnifier")
	
	def makeSettings(self, settingsSizer):
		sHelper = gui.guiHelper.BoxSizerHelper(self, sizer=settingsSizer)
		
		# Translators: This is the label for a combobox in the
		# Windows Magnifier settings panel.
		viewMoveLabelText = _("Report view moves:")
		self.viewMoveChoices = [
			# Translators: This is a combobox option in the settings panel.
			_("Off"),
			# Translators: This is a combobox option in the settings panel.
			_("With beeps"),
			# Translators: This is a combobox option in the settings panel.
			_("Vocal"),
		]
		self.viewMoveComboBox = sHelper.addLabeledControl(viewMoveLabelText, wx.Choice, choices=self.viewMoveChoices)
		try:
			index = self.viewMoveComboBox.index(config.conf["winmag"]["reportViewMoves"])
		except:
			index = 0
		self.viewMoveComboBox.SetSelection(index)
		
		# Translators: This is the label for a checkbox in the
		# Windows Magnifier settings panel.
		viewResizingText = _("Report the resizing of the view (docked and lense only)")
		#zzz self.viewResizingCheckBox = sHelper.addItem(wx.CheckBox, label=viewResizingText)
		#zzz self.viewResizingCheckBox = sHelper.addLabeledControl(viewResizingText, wx.CheckBox)
		#zzz self.viewResizingCheckBox.SetValue(config.conf["winmag"]["reportViewResizing"])
		
		self.viewResizingCheckBox = wx.CheckBox(self, label=viewResizingText)
		self.viewResizingCheckBox.SetValue(config.conf["winmag"]["reportViewResizing"])
		sHelper.addItem(self.viewResizingCheckBox)

	def onSave(self):
		config.conf["winmag"]["reportViewMoves"] = self.shapeCheckBox.IsChecked()
		config.conf["winmag"]["reportViewMoves"] = self.textUnits[self.viewResizingCheckBox.GetSelection()]
