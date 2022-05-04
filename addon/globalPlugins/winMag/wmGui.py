# -*- coding: UTF-8 -*-
# globalPlugins/winMag/gui.py
# NVDA add-on: Windows Magnifier
# Copyright (C) 2019-2021 Cyrille Bougot
#This file is covered by the GNU General Public License.
#See the file COPYING.txt for more details.

from __future__ import unicode_literals

from .msg import nvdaTranslation

import gui
from gui import guiHelper, nvdaControls
import config
from logHandler import log
from tones import beep
import math

import wx

import addonHandler

addonHandler.initTranslation()


class WinMagSettingsPanel(gui.SettingsPanel):
	# Translators: This is the label for the Windows Magnifier settings panel.
	title = _("Windows Magnifier")
	
	reportViewMoveAndScreenEdgesLabels = (
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
		sHelper = guiHelper.BoxSizerHelper(self, sizer=settingsSizer)
		
		# Translators: This is the label for a combobox in the Windows Magnifier settings panel.
		reportViewMoveLabelText = _("Report view &moves:")
		reportViewMoveChoices = [name for setting, name in self.reportViewMoveAndScreenEdgesLabels]
		self.reportViewMoveList = sHelper.addLabeledControl(reportViewMoveLabelText, wx.Choice, choices=reportViewMoveChoices)
		for index, (setting, name) in enumerate(self.reportViewMoveAndScreenEdgesLabels):
			if setting == config.conf["winMag"]["reportViewMove"]:
				self.reportViewMoveList.SetSelection(index)
				break
		else:
			log.debugWarning("Could not set report move list to current setting")
		self.reportViewMoveList.Bind(wx.EVT_CHOICE, self.onReportViewMoveChange)
		
		# Translators: This is the label for a combobox in the Windows Magnifier settings panel.
		reportScreenEdgesLabelText = _("Report screen &edges:")
		reportScreenEdgesChoices = [name for setting, name in self.reportViewMoveAndScreenEdgesLabels]
		self.reportScreenEdgesList = sHelper.addLabeledControl(reportScreenEdgesLabelText, wx.Choice, choices=reportScreenEdgesChoices)
		for index, (setting, name) in enumerate(self.reportViewMoveAndScreenEdgesLabels):
			if setting == config.conf["winMag"]["reportMoveToScreenEdges"]:
				self.reportScreenEdgesList.SetSelection(index)
				break
		else:
			log.debugWarning("Could not set report edges list to current setting")
		self.reportScreenEdgesList.Bind(wx.EVT_CHOICE, self.onReportScreenEdgesChange)

		# Translators: This is the label for a slider in the Windows Magnifier settings panel.
		toneVolumeLabelText = _('Volume of the tones indicating the &position of the view:')
		self.toneVolumeSlider = sHelper.addLabeledControl(
			toneVolumeLabelText,
			nvdaControls.EnhancedInputSlider,
			minValue=int(config.conf.getConfigValidation(("winMag", "toneVolume")).kwargs["min"]),
			maxValue=int(config.conf.getConfigValidation(("winMag", "toneVolume")).kwargs["max"]),
		)
		self.toneVolumeSlider.SetLineSize(1)
		self.toneVolumeSlider.SetPageSize(10)
		self.toneVolumeSlider.SetValue(config.conf["winMag"]["toneVolume"])
		self.updateToneVolumeSliderEnableState()
				
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
	
	def onReportViewMoveChange(self, evt):
		self.updateToneVolumeSliderEnableState()
		
	def onReportScreenEdgesChange(self, evt):
		self.updateToneVolumeSliderEnableState()
	
	def updateToneVolumeSliderEnableState(self):
		isTonesUsed = (
			self.reportViewMoveAndScreenEdgesLabels[self.reportViewMoveList.GetSelection()][0] == "tones"
			or self.reportViewMoveAndScreenEdgesLabels[self.reportScreenEdgesList.GetSelection()][0] == "tones"
		)
		self.toneVolumeSlider.Enable(isTonesUsed)

	def onPanelActivated(self):
		self.toneVolumeSlider.Bind(wx.EVT_SLIDER, self._onToneVolumeChange)
		self.updateToneVolumeSliderEnableState()
		super().onPanelActivated()
		
	def _onToneVolumeChange(self, evt):
		vol = evt.Int
		minPitch = config.conf['mouse']['audioCoordinates_minPitch']
		maxPitch = config.conf['mouse']['audioCoordinates_maxPitch']
		midPitch = minPitch * (2 ** (math.log(maxPitch / minPitch, 2)/2))
		beep(midPitch, 30, vol, vol)	
		
	def onSave(self):
		config.conf["winMag"]["reportViewMove"] = self.reportViewMoveAndScreenEdgesLabels[self.reportViewMoveList.GetSelection()][0]
		config.conf["winMag"]["reportMoveToScreenEdges"] = self.reportViewMoveAndScreenEdgesLabels[self.reportScreenEdgesList.GetSelection()][0]
		config.conf["winMag"]["toneVolume"] = self.toneVolumeSlider.Value
		config.conf['winMag']['reportTurnOnOff'] = self.reportTurnOnOffCheckBox.IsChecked()
		config.conf['winMag']['reportZoom'] = self.reportZoomCheckBox.IsChecked()
		config.conf['winMag']['reportColorInversion'] = self.reportColorInversionCheckBox.IsChecked()
		config.conf['winMag']['reportViewChange'] = self.reportViewChangeCheckBox.IsChecked()
		config.conf['winMag']['reportLensResizing'] = self.reportLensResizingCheckBox.IsChecked()
		config.conf["winMag"]["passCtrlAltArrow"] = self.passCtrlAltArrowLabels[self.passCtrlAltArrowList.GetSelection()][0]
		