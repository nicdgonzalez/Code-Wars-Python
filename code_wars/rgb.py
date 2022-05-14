"""
The rgb function is incomplete. Complete it so that passing in RGB decimal
values will result in a hexadecimal representation being returned. Valid
decimal values for RGB are 0 - 255. Any values that fall out of that range
must be rounded to the closest valid value.

Note: Your answer should always be 6 characters long, the shorthand
with 3 will not work here.

The following are examples of expected output values:
rgb(255, 255, 255)  # returns FFFFFF
rgb(255, 255, 300)  # returns FFFFFF
rgb(0,0,0)          # returns 000000
rgb(148, 0, 211)    # returns 9400D3
"""

from typing import Tuple


def rgb_to_hex(red: int, green: int, blue: int) -> str:
    """Converts RGB values into its hexidecimal representation. Valid decimal
    values for RGB range from 0 to 255. Any numbers that fall above or below
    that range will be rounded to the closest valid value.

    Parameters
    -----------
    red: :class:`int`
        Decimal value for the color Red. Valid values range from 0 to 255.
    green: :class:`int`
        Decimal value for the color Green. Valid values range from 0 to 255.
    blue: :class:`int`
        Decimal value for the color Blue. Valid values range from 0 to 255.

    Returns a :class:`str` representing the hexidecimal value of the RGB
    values input into the function. e.g., (148, 0, 211) returns '9400D3'.
    """

    def limit(value: int, *, min: int = 0, max: int = 255) -> int:
        from builtins import min as __min__
        from builtins import max as __max__

        return __min__(__max__(min, value), max)

    rgb: Tuple[int, ...] = (red, green, blue)
    to_hex: str = lambda color: format(limit(color, min=0, max=255), '02X')

    return ''.join(map(to_hex, rgb))


if __name__ == '__main__':
    print(rgb_to_hex(255, 255, 255))  # FFFFFF
    print(rgb_to_hex(255, 255, 300))  # FFFFFF
    print(rgb_to_hex(0, 0, 0))  # 000000
    print(rgb_to_hex(148, 0, 211))  # 9400D3
