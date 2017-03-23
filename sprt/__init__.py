"""
A Python package for Wald's sequential probability ratio test
"""
import sys as _sys
import os as _os

_sys.path.append(_os.path.abspath('../'))

__version__ = '0.01'
__author__ = 'Zhenning Yu'
__email__ = 'yuzhenning.bio@gmail.com'

from .sprt import SPRT, SPRTBinomial, SPRTNormal, SPRTPoisson
