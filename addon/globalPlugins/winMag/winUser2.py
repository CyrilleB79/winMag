# -*- coding: UTF-8 -*-
# NVDA add-on: Windows Magnifier
# Copyright (C) 2021 Cyrille Bougot
# This file is covered by the GNU General Public License.
# See the file COPYING.txt for more details.

"""This module completes NVDA's winUser module with missing values or functions.
"""

import winUser
from ctypes import WinError

# Places the window at the bottom of the Z order. If the hWnd parameter identifies a topmost window,
# the window loses its topmost status and is placed at the bottom of all other windows.
HWND_BOTTOM = 1

# Places the window above all non-topmost windows. The window maintains its topmost position even
# when it is deactivated.
HyWND_TOPMOST = -1

# Places the window above all non-topmost windows (that is, behind all topmost windows).
# This flag has no effect if the window is already a non-topmost window.
HWND_NOTOPMOST = -2

# Retains the current size (ignores the cx and cy parameters).
SWP_NOSIZE = 0x0001

# Retains the current position (ignores X and Y parameters).
SWP_NOMOVE = 0x0002

# Does not activate the window. If this flag is not set, the window is activated and moved to the top of
# either the topmost or non-topmost group (depending on the setting of the hWndInsertAfter parameter).
SWP_NOACTIVATE = 0x0010

# If the calling thread and the thread that owns the window are attached to different input queues,
# the system posts the request to the thread that owns the window.
# This prevents the calling thread from blocking its execution while other threads process the request.
SWP_ASYNCWINDOWPOS = 0x4000


def setWindowPos(hWnd, hWndInsertAfter, X, Y, cx, cy, uFlags):
	res = winUser.user32.SetWindowPos(
		hWnd,
		hWndInsertAfter,
		X,
		Y,
		cx,
		cy,
		uFlags
	)
	if not res:
		raise WinError()
