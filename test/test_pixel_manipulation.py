import numpy as np
import pytest
from bitlist import bitlist
from hypothesis import given
from hypothesis.extra.numpy import arrays
from hypothesis.strategies import integers
from numpy.typing import NDArray
from steganography.utils.pixel_manipulation import (
    combine_rgb_and_alpha,
    embed_bits_in_pixels,
    get_LSB_bytes_from_pixels,
    _seperate_rgb_and_alpha,
)

pixels = np.array(
    [
        [255, 0, 0, 255],
        [0, 255, 0, 100],
        [0, 0, 255, 50],
        [0, 0, 0, 0],
    ]
).flatten()

rgb = np.array(
    [
        [255, 0, 0],
        [0, 255, 0],
        [0, 0, 255],
        [0, 0, 0],
    ]
).flatten()

alpha = np.array([[255], [100], [50], [0]]).flatten()


def test_embed_bits_in_pixels() -> None:
    # TODO function tests
    with pytest.raises(ValueError):
        embed_bits_in_pixels(np.array([[1], [2]]), bitlist(""), 1)
        embed_bits_in_pixels(rgb, bitlist(""), 0)
        embed_bits_in_pixels(rgb, bitlist(""), 9)


def test_get_LSB_bytes_from_pixels() -> None:
    # TODO function tests

    with pytest.raises(ValueError):
        get_LSB_bytes_from_pixels(pixels, 0)
        get_LSB_bytes_from_pixels(pixels, 9)


def test_build_bytes_from_pixels() -> None:
    p1 = np.array([255, 255, 0, 0, 0, 0])
    p2 = np.array([0, 0, 0, 2])
    p3 = np.array([3])
    assert get_LSB_bytes_from_pixels(p1, 1) == b"0"
    assert get_LSB_bytes_from_pixels(p1, 2) == b"\x0f\x00"
    assert get_LSB_bytes_from_pixels(p2, 1) == b"\x00"
    assert get_LSB_bytes_from_pixels(p2, 2) == b"\x02"
    assert get_LSB_bytes_from_pixels(p3, 1) == b"\x01"
    assert get_LSB_bytes_from_pixels(p3, 2) == b"\x03"


def test_combine_rgb_and_alpha() -> None:
    assert np.array_equal(combine_rgb_and_alpha(rgb, alpha), pixels)
    with pytest.raises(ValueError):
        combine_rgb_and_alpha(rgb[1:], alpha)
        combine_rgb_and_alpha(rgb, alpha[1:])


def test_seperate_rgb_from_alpha() -> None:
    nrgb, nalpha = _seperate_rgb_and_alpha(pixels)
    assert np.array_equal(nrgb, rgb)
    assert np.array_equal(nalpha, alpha)
    with pytest.raises(ValueError):
        _seperate_rgb_and_alpha(pixels[1:])


@given(
    integers(min_value=1, max_value=1000)
    .filter(lambda x: x % 4 == 0)
    .flatmap(lambda n: arrays(int, n))
)
def test_seperate_and_combine_reversal_int(a: NDArray) -> None:
    assert np.array_equal(a, combine_rgb_and_alpha(*_seperate_rgb_and_alpha(a)))


@given(
    integers(min_value=1, max_value=1000)
    .filter(lambda x: x % 4 == 0)
    .flatmap(lambda n: arrays(str, n))
)
def test_seperate_and_combine_reversal_str(a: NDArray) -> None:
    assert np.array_equal(a, combine_rgb_and_alpha(*_seperate_rgb_and_alpha(a)))


@given(
    arrays(int, 100, elements=integers()),
    integers(min_value=1, max_value=8),
    integers(min_value=1, max_value=10 ^ 8),
)
def set_get_lsb_bytes_from_pixels_reversal(pixels: NDArray, n_lsb: int, bits: int):
    assert bits == get_LSB_bytes_from_pixels(
        embed_bits_in_pixels(pixels, bits, n_lsb), n_lsb
    )
