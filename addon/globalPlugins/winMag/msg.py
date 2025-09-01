# -*- coding: UTF-8 -*-
# A simple module to bypass the addon translation system,
# so it can take advantage from the NVDA translations directly.
# This module was copied from Alberto Buffolino's columnsReview add-on
# (https://github.com/ABuffEr/columnsReview)


def nvdaTranslation(message):
	return _(message)
