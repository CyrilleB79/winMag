# A part of NonVisual Desktop Access (NVDA)
# This file is covered by the GNU General Public License.
# See the file COPYING for more details.
# Copyright (C) 2020 Cyrille Bougot, NV Access Limited

import winVersion
from ctypes import Structure, windll, c_float, POINTER, WINFUNCTYPE, WinError
from ctypes.wintypes import BOOL
from ctypes.wintypes import HWND, INT, FLOAT
try:
	from ctypes.wintypes import PINT, PRECT, PFLOAT
except ImportError:
	from ctypes.wintypes import POINTER, RECT
	PINT = POINTER(INT)
	PRECT = POINTER(RECT)
	PFLOAT = POINTER(FLOAT)

class MAGCOLOREFFECT(Structure):
	_fields_ = (("transform", c_float * 5 * 5),)


# homogeneous matrix for a 4-space transformation (red, green, blue, opacity).
# https://docs.microsoft.com/en-gb/windows/win32/gdiplus/-gdiplus-using-a-color-matrix-to-transform-a-single-color-use
TRANSFORM_BLACK = MAGCOLOREFFECT()
TRANSFORM_BLACK.transform[4][4] = 1.0


def _errCheck(result, func, args):
	if result == 0:
		raise WinError()
	return args


class Magnification:
	"""Static class that wraps necessary functions from the Windows magnification API."""

	_magnification = windll.Magnification

	# Set full screen color effect
	_MagSetFullscreenColorEffectFuncType = WINFUNCTYPE(BOOL, POINTER(MAGCOLOREFFECT))
	_MagSetFullscreenColorEffectArgTypes = ((1, "effect"),)

	# Get full screen color effect
	_MagGetFullscreenColorEffectFuncType = WINFUNCTYPE(BOOL, POINTER(MAGCOLOREFFECT))
	_MagGetFullscreenColorEffectArgTypes = ((2, "effect"),)

	# SetFullscreenTransform
	_MagSetFullscreenTransformFuncType = WINFUNCTYPE(BOOL, FLOAT, INT, INT)
	_MagSetFullscreenTransformArgTypes = ((1, "magLevel"), (1, "xOffset"), (1, "yOffset"))

	# GetFullscreenTransform
	_MagGetFullscreenTransformFuncType = WINFUNCTYPE(BOOL, PFLOAT, PINT, PINT)
	_MagGetFullscreenTransformArgTypes = ((2, "MagLevel"), (2, "xOffset"), (2, "yOffset"))

	# show system cursor
	_MagShowSystemCursorFuncType = WINFUNCTYPE(BOOL, BOOL)
	_MagShowSystemCursorArgTypes = ((1, "showCursor"),)
	
	# GetWindowSource
	_MagGetWindowSourceFuncType = WINFUNCTYPE(BOOL, HWND, PRECT)
	_MagGetWindowSourceArgTypes = ((1, "hwnd"), (2, "pRect"))

	# initialize
	_MagInitializeFuncType = WINFUNCTYPE(BOOL)
	MagInitialize = _MagInitializeFuncType(("MagInitialize", _magnification))
	MagInitialize.errcheck = _errCheck

	# uninitialize
	_MagUninitializeFuncType = WINFUNCTYPE(BOOL)
	MagUninitialize = _MagUninitializeFuncType(("MagUninitialize", _magnification))
	MagUninitialize.errcheck = _errCheck

	# These magnification functions are not available on versions of Windows prior to Windows 8,
	# and therefore looking them up from the magnification library will raise an AttributeError.
	try:
		MagSetFullscreenColorEffect = _MagSetFullscreenColorEffectFuncType(
			("MagSetFullscreenColorEffect", _magnification),
			_MagSetFullscreenColorEffectArgTypes
		)
		MagSetFullscreenColorEffect.errcheck = _errCheck
		MagGetFullscreenColorEffect = _MagGetFullscreenColorEffectFuncType(
			("MagGetFullscreenColorEffect", _magnification),
			_MagGetFullscreenColorEffectArgTypes
		)
		MagGetFullscreenColorEffect.errcheck = _errCheck
		MagSetFullscreenTransform = _MagSetFullscreenTransformFuncType(
			("MagSetFullscreenTransform", _magnification),
			_MagSetFullscreenTransformArgTypes
		)
		MagSetFullscreenTransform.errcheck = _errCheck
		MagGetFullscreenTransform = _MagGetFullscreenTransformFuncType(
			("MagGetFullscreenTransform", _magnification),
			_MagGetFullscreenTransformArgTypes
		)
		MagGetFullscreenTransform.errcheck = _errCheck
		MagShowSystemCursor = _MagShowSystemCursorFuncType(
			("MagShowSystemCursor", _magnification),
			_MagShowSystemCursorArgTypes
		)
		MagShowSystemCursor.errcheck = _errCheck
		
		MagGetWindowSource = _MagGetWindowSourceFuncType(
			("MagGetWindowSource", _magnification),
			_MagGetWindowSourceArgTypes
		)
		MagGetWindowSource.errcheck = _errCheck
	except AttributeError:
		MagSetFullscreenColorEffect = None
		MagGetFullscreenColorEffect = None
		MagSetFullscreenTransform = None
		MagGetFullscreenTransform = None
		MagShowSystemCursor = None


