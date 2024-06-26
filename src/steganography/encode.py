from __future__ import annotations

from typing import Optional

import numpy as np
from numpy.typing import NDArray
from PIL import Image
from PIL.Image import Image as Img

from steganography._logging import logger
from steganography.bit_format import STEG_TAG, build_bits_for_file, get_max_payload_size
from steganography.utils.bit_manipulation import set_lsb_bit
from steganography.utils.hashing import hash_file
from steganography.utils.misc import (
    DEFAULT_ENCRYPTION_KEY,
    HashFunction,
    PayloadSizeError,
)
from steganography.utils.pixel_manipulation import (
    build_pixel_array,
    combine_rgb_and_alpha,
    embed_bits_in_pixels,
    encode_image_to_rgb_and_alpha_array,
)

__all__ = ["encode_file_in_image"]


def _encode_file_in_pixels(
    pixels: NDArray,
    file_content: bytes,
    file_name: str,
    encryption_key: bytes,
    n_lsb: int,
    hash_func: Optional[HashFunction],
    compression: bool = True,
) -> NDArray:
    """encode the file and Metadata into a flattened rgb-array"""
    # Get the max_size
    max_size = get_max_payload_size(pixels, n_lsb)
    # Convert raw bytes into the STEG-byte_format
    logger.debug("constructing the bits for encoding")
    bits = build_bits_for_file(
        file_content,
        file_name,
        hash_func,
        encryption_key,
        steg_tag=STEG_TAG,
        compression=compression,
    )
    if len(bits) > max_size:
        # Check if those bits would be to big
        logger.debug(
            "The new Image is to big to store into the Coverimage. Throwing PayloadSizeError"
        )
        raise PayloadSizeError(
            "the File and filename are too big to store into the Image"
        )
    # write the bits to the pixel array
    logger.debug("starting the embeding process")
    embeded_pixels = embed_bits_in_pixels(pixels, bits, n_lsb)
    logger.debug("finished the embeding process")
    return embeded_pixels


def encode_file_in_image(
    file_bytes: bytes,
    file_name: str,
    image: Img,
    n_lsb: int,
    encryption_key: Optional[str] = None,
    hashing: bool = True,
    compression: bool = True,
) -> Img:
    """
    Encode file into image
    :param file: the file you intend to hide
    :param file_name: the filename
    :param image: Coverimage which is modified
    :param n_lsb: the number of least significant bits which are modified
    :param encryption_key: the key used for encryption. If it is not specified, a default key is used.
    :return: Modified Image
    """
    if not isinstance(file_name, str):
        raise ValueError("The filename must be of type 'str'")
    if not isinstance(file_bytes, bytes):
        raise ValueError("The file_bytes must be of type 'bytes'")
    if encryption_key is None:
        AES_key = DEFAULT_ENCRYPTION_KEY
    else:
        AES_key = bytes(encryption_key.encode())
    hash_func: Optional[HashFunction] = hash_file if hashing else None
    # Get Image Dimensions
    width, height = image.size
    mode = image.mode
    logger.debug(f"reading the imagesize; got:{width}x{height}  mode: {mode}")
    # read and seperate the RGB and Alpha values from the Image
    logger.debug("spliting the Image into RGB and Alpha channel")
    argb, alphas = encode_image_to_rgb_and_alpha_array(image)
    # reserve the first pixel for encoding the n_lsb value
    rgb = argb[1:]
    lsb_val = argb[0]
    # Modify the first pixel by writing the n_lsb value
    logger.debug("writing the n_lsb value into the first 3 bits")
    new_lsb_val = set_lsb_bit(lsb_val, n_lsb)
    # Modify the other pixels by writing the bytes of the file
    logger.info(f"Writing the payload into the last {n_lsb} bits of the Coverimage")
    embeded_rgb = _encode_file_in_pixels(
        rgb, file_bytes, file_name, AES_key, n_lsb, hash_func, compression
    )
    # combine the modified- and NLSB pixels and insert the alpha values
    new_rgb: NDArray = np.insert(embeded_rgb, 0, new_lsb_val)
    # if mode != "RGBA":
    logger.debug("reconstructing the full RGBA image from the 2 chanels")
    new_flatt_image_array = combine_rgb_and_alpha(new_rgb, alphas)
    # reconstruct the Dimensions from the flatt array
    logger.info("creating new Image from the pixels")
    new_image_array = build_pixel_array(new_flatt_image_array, width, height)
    return Image.fromarray(new_image_array)  # type: ignore
