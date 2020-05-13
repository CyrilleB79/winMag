# -*- coding: UTF-8 -*-
#globalPlugins/winMag.py
#NVDA add-on: Windows Magnifier
#Copyright (C) 2019-2020 Cyrille Bougot
#This file is covered by the GNU General Public License.
#See the file COPYING.txt for more details.

from __future__ import unicode_literals

import config
import addonHandler

addonHandler.initTranslation()

# Identifiers of the possible setting options to report view moves.
REPORT_VIEW_MOVES_OFF = "Off"
REPORT_VIEW_MOVES_WITH_BEEPS = "WithBeeps"
REPORT_VIEW_MOVES_VOCAL = "Vocal"
# Report view move choices associated with their user readable and translatable labels
moveViewReportOptions = [
	# Translators: The label for a report view move setting.
	(REPORT_VIEW_MOVES_OFF, _("Off")),
	# Translators: The label for a report view move setting.
	(REPORT_VIEW_MOVES_WITH_BEEPS, _("With beeps")),
	# Translators: The label for a report view move setting.
	(REPORT_VIEW_MOVES_VOCAL, _("Vocal")),
]

confspec = {
	"reportViewMoves": "option({oOff}, {oWithBeeps}, {oVocal}, default={oVocal})".format(
		oOff=REPORT_VIEW_MOVES_OFF, oWithBeeps=REPORT_VIEW_MOVES_WITH_BEEPS, oVocal=REPORT_VIEW_MOVES_VOCAL
	),
	"reportViewResizing": 'boolean(default=true)',
}
config.conf.spec["winmag"] = confspec

