from bitlist import bitlist
from more_itertools import chunked
import numpy as np
from numpy.typing import NDArray
from steganography.utils.bit_manipulation import set_LSB
from copy import deepcopy
from typing import Tuple


__all__ = [
    "embed_bits_in_pixels",
    "build_pixel_array",
    "combine_rgb_and_alpha",
    "seperate_rgb_and_alpha",
    "get_LSB_bytes_from_pixels",
]


def embed_bits_in_pixels(pixels: NDArray, bits: bitlist, n_LSB: int) -> NDArray:
    new = deepcopy(pixels)
    for i, el in enumerate(zip(pixels, chunked(bits, n_LSB))):
        p, lsb = el
        p = set_LSB(p, n_LSB, lsb)
        new[i] = p
    return new


def build_pixel_array(pixels: NDArray, widht: int, height: int) -> NDArray:
    pixels = pixels.reshape(height, widht, 4)
    return pixels


def combine_rgb_and_alpha(rgb: NDArray, alpha: NDArray) -> NDArray:
    n: list = []
    for p, a in zip(chunked(rgb, 3), alpha):
        n.extend(p)
        n.append(a)
    return np.array(n)


def seperate_rgb_and_alpha(img_pixels: NDArray) -> Tuple[NDArray, NDArray]:
    pixels = img_pixels.flatten()
    rgb = []
    alpha = []

    for r, g, b, a in chunked(pixels, 4):
        rgb.append(r)
        rgb.append(g)
        rgb.append(b)
        alpha.append(a)
    return np.array(rgb), np.array(alpha)


def get_LSB_bytes_from_pixels(pixels: NDArray, n_lsb: int) -> bytes:
    bits: str = ""
    for p in pixels:
        pb = bitlist(int(p), length=p + n_lsb)
        bits += pb[-n_lsb:].bin()
    return bitlist(bits).to_bytes()
