"""@package i2c_lcd
Top-level namespace for the i2c_lcd module
"""

#pylint: disable=too-few-public-methods

from .i2c_lcd import Display, RGBDisplay

__version__ = '2.0.1'

__all__ = [
    'Display',
    'RGBDisplay',
]
