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
	
	reportViewMoveLabels = (
		# Translators: An option in the combobox "Report view moves" in winMag setting panel.
		("off", _("Off")),
		# Translators: An option in the combobox "Report view moves" in winMag setting panel.
		("speech", _("With speech")),
		# Translators: An option in the combobox "Report view moves" in winMag setting panel.
		("tones", _("With tones")),
	)
	passCtrlAltArrowLabels = (
		# Translators: An option in the combobox that configures passing control+alt+arrow in winMag setting panel.
		("never", _("Never")),
		# Translators: An option in the combobox that configures passing control+alt+arrow in winMag setting panel.
		("whenNotInTable", _("Only when not in table")),
		# Translators: An option in the combobox that configures passing control+alt+arrow in winMag setting panel.
		("always", _("Always")),
	)

	def makeSettings(self, settingsSizer):
		sHelper = gui.guiHelper.BoxSizerHelper(self, sizer=settingsSizer)
		
		# Translators: This is the label for a combobox in the Windows Magnifier settings panel.
		reportViewMoveLabelText = _("Report view &moves:")
		reportViewMoveChoices = [name for setting, name in self.reportViewMoveLabels]
		self.reportViewMoveList = sHelper.addLabeledControl(reportViewMoveLabelText, wx.Choice, choices=reportViewMoveChoices)
		for index, (setting, name) in enumerate(self.reportViewMoveLabels):
			if setting == config.conf["winMag"]["reportViewMove"]:
				self.reportViewMoveList.SetSelection(index)
				break
		else:
			log.debugWarning("Could not set report move list to current setting")
		
		#zzz self.reportEdges = 

		self.reportTurnOnOffCheckBox = sHelper.addItem(
			# Translators: This is the label for a checkbox in the Windows Magnifier settings panel.
			wx.CheckBox(self, label=_("Report &turn on or off"))
		)
		self.reportTurnOnOffCheckBox.SetValue(config.conf['winMag']['reportTurnOnOff'])

		self.reportZoomCheckBox = sHelper.addItem(
			# Translators: This is the label for a checkbox in the Windows Magnifier settings panel.
			wx.CheckBox(self, label=_("Report &zoom"))
		)
		self.reportZoomCheckBox.SetValue(config.conf['winMag']['reportZoom'])
		
		self.reportColorInversionCheckBox = sHelper.addItem(
			# Translators: This is the label for a checkbox in the Windows Magnifier settings panel.
			wx.CheckBox(self, label=_("Report color &inversion"))
		)
		self.reportColorInversionCheckBox.SetValue(config.conf['winMag']['reportColorInversion'])
		
		self.reportViewChangeCheckBox = sHelper.addItem(
			# Translators: This is the label for a checkbox in the Windows Magnifier settings panel.
			wx.CheckBox(self, label=_("Report &view change"))
		)
		self.reportViewChangeCheckBox.SetValue(config.conf['winMag']['reportViewChange'])
		
		self.reportLensResizingCheckBox = sHelper.addItem(
			# Translators: This is the label for a checkbox in the Windows Magnifier settings panel.
			wx.CheckBox(self, label=_("Report &lens or docked window resizing"))
		)
		self.reportLensResizingCheckBox.SetValue(config.conf['winMag']['reportLensResizing'])
		
		# Translators: This is the label for a combobox in the Windows Magnifier settings panel.
		passCtrlAltArrowLabelText = _("In &documents and list views, pass control+alt+arrows shortcuts to Windows Magnifier:")
		passCtrlAltArrowChoices = [name for setting, name in self.passCtrlAltArrowLabels]
		self.passCtrlAltArrowList = sHelper.addLabeledControl(passCtrlAltArrowLabelText, wx.Choice, choices=passCtrlAltArrowChoices)
		for index, (setting, name) in enumerate(self.passCtrlAltArrowLabels):
			if setting == config.conf["winMag"]["passCtrlAltArrow"]:
				self.passCtrlAltArrowList.SetSelection(index)
				break
		else:
			log.debugWarning("Could not set pass control alt arrow list to current setting")
	
	def onSave(self):
		config.conf["winMag"]["reportViewMove"] = self.reportViewMoveLabels[self.reportViewMoveList.GetSelection()][0]
		config.conf['winMag']['reportTurnOnOff'] = self.reportTurnOnOffCheckBox.IsChecked()
		config.conf['winMag']['reportZoom'] = self.reportZoomCheckBox.IsChecked()
		config.conf['winMag']['reportColorInversion'] = self.reportColorInversionCheckBox.IsChecked()
		config.conf['winMag']['reportViewChange'] = self.reportViewChangeCheckBox.IsChecked()
		config.conf['winMag']['reportLensResizing'] = self.reportLensResizingCheckBox.IsChecked()
		config.conf["winMag"]["passCtrlAltArrow"] = self.passCtrlAltArrowLabels[self.passCtrlAltArrowList.GetSelection()][0]
		