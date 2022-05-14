"""
ATM machines allow 4 or 6 digit PIN codes and PIN codes cannot contain
anything but exactly 4 digits or exactly 6 digits.

If the function is passed a valid PIN string, return true, else return false.

Examples
"1234"   -->  true
"12345"  -->  false
"a234"   -->  false
"""

from re import match


def validate_pin(pin: str) -> bool:
    """Checks whether the pin is a valid 4 or 6 digit pin.
    
    Parameters
    -----------
    pin: :class:`str`
        A (4) or (6) digit pin containing only numbers.

    Returns :class:`True` if it is a valid pin or :class:`False` if not.
    """

    return ((len(pin) in [4, 6])
            and (match(r'^\d{4}(\d{2})?$', pin) is not None))


if __name__ == '__main__':
    print(validate_pin('1234'))  # True
    print(validate_pin('12345'))  # False
    print(validate_pin('A123'))  # False
