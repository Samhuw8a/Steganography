from __future__ import annotations
import sys
import numpy as np
from numpy.typing import NDArray
from PIL import Image


def calculate_mse(original: NDArray, modified: NDArray) -> int:
    diff = np.subtract(original, modified)
    mse = np.mean(np.square(diff))
    return mse


def calculate_psnr(original: NDArray, modified: NDArray) -> float:
    mse = calculate_mse(original, modified)
    if mse == 0:
        return 100
    max_pixel_value = 255.0
    psnr = 20 * np.log10(max_pixel_value) - 10 * np.log10(mse)
    return psnr


def main() -> int:
    """
    Test images from wikipedia: https://en.wikipedia.org/wiki/Peak_signal-to-noise_ratio
    comp-90: 45.53
    comp-30: 36.81
    comp-10: 31.45
    """
    args = sys.argv
    assert len(args) == 3

    orig = np.array(Image.open(args[1]))
    comp = np.array(Image.open(args[2]))
    mse = calculate_mse(orig, comp)
    psnr = calculate_psnr(orig, comp)
    print(f"MSE: {mse}")
    print(f"PSNR: {psnr}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
