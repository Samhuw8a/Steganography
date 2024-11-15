"""
A Collection of Functions regarding setting and reading LSB bits from pixel values
"""
from __future__ import annotations

from collections.abc import MutableSequence
from typing import Union, TypeVar

from steganography._logging import logger
from steganography.utils.misc import FileError

from bitlist import bitlist
from more_itertools import chunked


__all__ = ["set_bit", "set_LSB", "set_lsb_bit"]


T = TypeVar("T")


def convert_bitlist_to_bytes(bits: str) -> bytes:
    # TODO Optimize
    conv_bytes = bytes()
    total = len(bits)
    logger.debug(f"Get Lenth of all Bits: {total}")
    for b in chunked(bits, 8):
        byte = int("".join(map(str, b)), 2).to_bytes(1, "big")
        # byte = bitlist(b).to_bytes()
        if conv_bytes.count(bytes(b"[STEG]")) == 2:
            return conv_bytes
        conv_bytes += byte

    # Validate that there are valid Tags
    if conv_bytes.count(bytes(b"[STEG]")) == 1:
        # If there is only one Tag, there might have been a wrong assumption on the user end
        raise FileError("The File is not decoded correctly. Try again with --no-hash")
    else:
        # If there are no tags the Image is not compatible with this Program
        raise FileError("The File is not compatible with this Programm.")


def set_lsb_bit(pixel: int, n_lsb: int) -> int:
    bits = bitlist(n_lsb - 1, length=3)[::-1]
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
        # If x is True, do nothing (XOR with 0). If x is False, use the mask for clearing the bit indicated by the mask (XOR with 1 in the requested position).
    ) * mask
    return v


def _pad_sequence_with_last_el(
    seq: MutableSequence[T], length: int
) -> MutableSequence[T]:
    """pad a Sequence with to last elements so that it is the given length"""
    padding_len: int = length - len(seq)
    last: T = seq[:-1]  # type:ignore
    if padding_len > 0:
        seq.extend(last for i in range(padding_len))
    assert len(seq) == length
    return seq


def set_LSB(v: int, n: int, x: MutableSequence[Union[int, bool]]) -> int:
    """set the n LSB's to the corresponding value in x"""
    if len(x) > n:
        raise ValueError("x must contain n elements")
    elif not 0 < n <= 8:
        raise ValueError("n has to be between 1 and 8")
    elif len(x) < n:
        x = _pad_sequence_with_last_el(x, n)
    for i in range(n):
        v = set_bit(v, i, x[i])
    return v
