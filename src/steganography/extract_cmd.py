from __future__ import annotations

from argparse import Namespace

from PIL import Image, UnidentifiedImageError

from steganography.decode import decode_file_from_image


def extract(args: Namespace) -> int:
    image_path = args.file
    # Check if the provided path is valid
    if not image_path.exists():
        raise FileNotFoundError(f"The image {image_path} does not exists")
    if args.password is not None:
        encryption_key = args.password.encode()
    else:
        encryption_key = None
    hashing = not args.no_hash
    try:
        image = Image.open(image_path)
    except UnidentifiedImageError:
        # Check if the Image can be opened
        raise FileNotFoundError(f"{image_path} is not a valid Image")

    # Decode the file from the image pixels
    file_name, file_bytes = decode_file_from_image(image, encryption_key, hashing)
    with open(file_name, "wb") as f:
        # write the file
        f.write(file_bytes)
    return 0
