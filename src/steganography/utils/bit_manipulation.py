from __future__ import annotations
from collections.abc import Sequence
from bitlist import bitlist
from typing import Union

__all__ = ["set_bit", "set_LSB", "set_lsb_bit"]


def set_lsb_bit(pixel: int, n_lsb: int) -> int:
    bits = bitlist(n_lsb - 1, length=3)
    return set_LSB(pixel, 3, list(bits))


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


def set_LSB(v: int, n: int, x: Sequence[Union[int, bool]]) -> int:
    """set the n LSB's to the corresponding value in x"""
    if len(x) != n:
        raise ValueError("x must contain n elements")
    if not 0 < n <= 8:
        raise ValueError("n has to be between 1 and 8")
    for i in range(n):
        v = set_bit(v, i, x[i])
    return v
