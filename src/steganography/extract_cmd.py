from __future__ import annotations

from argparse import Namespace

from PIL import Image, UnidentifiedImageError

from steganography._logging import logger
from steganography.decode import decode_file_from_image


def extract(args: Namespace) -> int:
    image_path = args.file
    logger.debug(f"loading the image_path. got: image_path = {image_path}")
    # Check if the provided path is valid
    if not image_path.exists():
        logger.debug("image_path does not exist. Throwing FileNotFoundError")
        raise FileNotFoundError(f"The image {image_path} does not exists")
    if args.password is not None:
        encryption_key = args.password.encode()
    else:
        encryption_key = None
    hashing = not args.no_hash
    logger.debug("loading all the nescecary args.")
    try:
        logger.info("loading the Image into memory")
        image = Image.open(image_path)
    except UnidentifiedImageError:
        # Check if the Image can be opened
        logger.debug("Image can't be opened. Throwing FileNotFoundError")
        raise FileNotFoundError(f"{image_path} is not a valid Image")

    # Decode the file from the image pixels
    logger.info("decoding File and meta data from Image")
    file_name, file_bytes = decode_file_from_image(image, encryption_key, hashing)
    with open(file_name, "wb") as f:
        # write the file
        logger.info("writing hidden File to disk")
        f.write(file_bytes)
    return 0
