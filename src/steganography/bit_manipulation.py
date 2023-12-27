from typing import Union
from collections.abc import Sequence


def set_bit(v: int, index: int, x: Union[int, bool]) -> int:
    """Set the index:th bit of v to 1 if x is truthy, else to 0, and return the new value."""
    # copied from: https://stackoverflow.com/questions/12173774/how-to-modify-bits-in-an-integer
    if isinstance(x, int) and x not in (0, 1):
        raise ValueError("x must be 1 or 0")

    mask = 1 << index  # Compute mask, an integer with just bit 'index' set.
    v |= mask  # Set the bit indicated by the mask to True.
    v ^= (
        not x
    ) * mask  # If x is True, do nothing (XOR with 0). If x is False, use the mask for clearing the bit indicated by the mask (XOR with 1 in the requested position).
    return v


def set_n_LSB(v: int, n: int, x: Sequence[Union[int, bool]]) -> int:
    """set the n LSB to the corresponding vallue in x"""
    if len(x) != n:
        raise ValueError("x must contain n elements")
    for i in range(n):
        v = set_bit(v, i, x[i])
    return v