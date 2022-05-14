"""
Find the odd int

Given an array of integers, find the one that appears an odd number of times.

There will always be only one integer that appears an odd number of times.
"""

from typing import List

# Sample test cases:
sample1 = [20, -1, 2, -2, 5, 5, 3, 3, 5, 5, 1, 2, 4, 4, 20, -1, -2]
sample2 = [1, 1, 2, -2, 5, 2, 4, 4, -1, -2, 5]


def find_it(sequence: List[int]) -> List[int]:
    """Given an array, find the values that appear an odd number of times.

    Parameters
    -----------
    sequence: :class:`list`
        An array of values to search through.

    Returns a :class:`list` of the odd values.
    """

    return list(set([value for value
                     in sequence
                     if (sequence.count(value) % 2) != 0]))


if __name__ == '__main__':
    print('Result of sample1:', find_it(sample1))  # [1]
    print('Result of sample2:', find_it(sample2))  # [-1]
