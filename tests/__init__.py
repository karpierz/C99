# Copyright (c) 2018 Adam Karpierz
# SPDX-License-Identifier: Zlib

from __future__ import absolute_import

__all__ = ('top_dir', 'test_dir')

import sys, os, importlib
if sys.version_info.major <= 2:  # pragma: no cover
    sys.modules["unittest.mock"] = importlib.import_module("mock")
sys.dont_write_bytecode = True
test_dir = os.path.dirname(os.path.abspath(__file__))
top_dir = os.path.dirname(test_dir)
del sys, os, importlib
