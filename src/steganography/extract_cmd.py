from __future__ import annotations
from argparse import Namespace
from steganography.decode import decode_file_from_image
from PIL import Image


def extract(args: Namespace) -> int:
    image_path = args.file
    encryption_key = args.password
    hashing = not args.no_hash
    image = Image.open(image_path)

    file_name, file_bytes = decode_file_from_image(image, encryption_key, hashing)
    with open(file_name, "wb") as f:
        f.write(file_bytes)
    return 0
