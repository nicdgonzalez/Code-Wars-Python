"""
Take a Ten Minute Walk

You live in the city of Cartesia where all roads are laid out in a perfect
grid. You arrived ten minutes too early to an appointment, so you decided to
take the opportunity to go for a short walk. The city provides its citizens
with a Walk Generating App on their phones -- everytime you press the button
it sends you an array of one-letter strings representing directions to walk
(eg. ['n', 's', 'w', 'e']). You always walk only a single block for each
letter (direction) and you know it takes you one minute to traverse one city
block, so create a function that will return true if the walk the app gives
you will take you exactly ten minutes (you don't want to be early or late!)
and will, of course, return you to your starting point. Return false
otherwise.

Note: you will always receive a valid array containing a random assortment
of direction letters ('n', 's', 'e', or 'w' only). It will never give you an
empty array (that's not a walk, that's standing still!).
"""

from typing import List

# Sample test cases:
sample_walk1: List[str] = ['e', 'w', 's', 'n', 'w', 'n', 's', 'w', 'e', 'e']
sample_walk2: List[str] = ['n', 'e', 'n', 's', 'n', 's', 'n', 's', 'n', 's']
sample_walk3: List[str] = ['n', 'w', 'n', 's', 'n', 's', 'n', 's', 'e', 's']
sample_walk4: List[str] = ['w', 'e', 'w', 'e', 'w', 'e', 'w', 'e', 'w', 'e',
                           'w', 'e']


def is_valid_walk(walk: List[str]) -> bool:
    """Determines whether the walk sequence is a valid walk. A valid walk
    consists of (10) directions and returns to its starting position.

    Parameters
    -----------
    walk: :class:`list`
        A sequence of directions with :class:`str` values that represent
        a direction to walk in; i.e., 'n', 'e', 's', 'w' represent
        North, East, South and West respectively.

    Returns :bool:`True` if the walk is a valid walk, :bool:`False` if not.
    """

    return ((len(walk) == 10)
            and (walk.count('n') == walk.count('s'))
            and (walk.count('e') == walk.count('w')))
