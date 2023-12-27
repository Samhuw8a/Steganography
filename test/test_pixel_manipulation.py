import numpy as np
from steganography.utils.pixel_manipulation import (
    embed_bits_in_pixels,
    combine_rgb_and_alpha,
    seperate_rgb_from_alpha,
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
    NotImplemented


def test_combine_rgb_and_alpha() -> None:
    assert np.array_equal(combine_rgb_and_alpha(rgb, alpha), pixels)


def test_seperate_rgb_from_alpha() -> None:
    nrgb, nalpha = seperate_rgb_from_alpha(pixels)
    assert np.array_equal(nrgb, rgb)
    assert np.array_equal(nalpha, alpha)
