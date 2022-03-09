from ast import Import
import os
import sys
import urllib.request

# PREWORK (don't modify): import colors, save to temp file and import
tmp = os.getenv("TMP", "/tmp")
color_values_module = os.path.join(tmp, 'color_values.py')
urllib.request.urlretrieve(
    'https://bites-data.s3.us-east-2.amazonaws.com/color_values.py',
    color_values_module
)
sys.path.append(tmp)

# should be importable now
from color_values import COLOR_NAMES  # noqa E402

class Color:
    """Color class.

    Takes the string of a color name and returns its RGB value.
    """

    def __init__(self, color: str):
        self.color: str = color
        print(COLOR_NAMES)
        self.rgb: tuple = COLOR_NAMES[color.upper()] if color.upper() in COLOR_NAMES else None

    @staticmethod
    def hex2rgb(hex: str) -> tuple:
        """Class method that converts a hex value into an rgb one"""
        try:
            if len(hex) != 7:
                raise ValueError()
            rgb = tuple(int(hex[i:i+2], 16) for i in (1, 3, 5))
            return rgb
        except ValueError:
            raise ValueError('hex2rgb received invalid parameter')

    @staticmethod
    def rgb2hex(rgb: tuple) -> str:
        """Class method that converts an rgb value into a hex one"""
        try:
            if len(rgb) != 3 or any(color > 255 or color < 0 for color in rgb):
                raise ValueError
            _hex = ''.join(['#'] + [hex(code)[2:] if len(hex(code)) == 4 else hex(code)[2:] + '0' for code in rgb])
            return _hex
        except ValueError:
            raise ValueError('rgb2hex received invalid parameter')

    def __repr__(self) -> str:
        """Returns the repr of the object"""
        return f"{type(self).__name__}('{self.color}')"

    def __str__(self) -> str:
        """Returns the string value of the color object"""
        return str(self.rgb) if self.rgb else 'Unknown'