from __future__ import annotations
from argparse import Namespace
from PIL import Image
from steganography.encode import encode_file_in_image


def embed(args: Namespace) -> int:
    image_path = args.target
    file = args.payload
    file_name = file.name
    n_lsb = args.lsb
    hashing = not args.no_hash
    encryption_key = args.password
    new_name = image_path.name
    if args.output is not None:
        new_name = args.output
        # ----
        image = Image.open(image_path)
        # TODO catch Exception
    with file.open("rb") as f:
        file_bytes = f.read()
        new_image = encode_file_in_image(
            file_bytes, file_name, image, n_lsb, encryption_key, hashing
        )
        new_image.save(new_name)
    return 0
