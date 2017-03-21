"""Python package for Wald's sequentially probability ratio test (SPRT)"""
import sys as _sys
import os as _os

_sys.path.append(_os.path.abspath('../'))

__version__ = '0.0.1'
__author__ = 'Zhenning Yu'
__email__ = 'yuzhenning.bio@gmail.com'
__all__ = ['SPRTBinomial']
