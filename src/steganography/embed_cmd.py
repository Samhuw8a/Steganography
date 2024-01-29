from __future__ import annotations

from argparse import Namespace

from PIL import Image, UnidentifiedImageError

from steganography.encode import encode_file_in_image


def embed(args: Namespace) -> int:
    image_path = args.target
    if not image_path.exists():
        raise FileNotFoundError(f"The image {image_path} does not exist")
    file = args.payload
    if not file.exists():
        raise FileNotFoundError(f"The file {file} does not exist")
    file_name = file.name
    n_lsb = args.lsb
    hashing = not args.no_hash
    encryption_key = args.password
    new_name = image_path.name
    if args.output is not None:
        new_name = args.output
    try:
        image = Image.open(image_path)
    except UnidentifiedImageError:
        raise FileNotFoundError(f"{image_path} is not a valid Image")

    with file.open("rb") as f:
        file_bytes = f.read()
        new_image = encode_file_in_image(
            file_bytes, file_name, image, n_lsb, encryption_key, hashing
        )
        new_image.save(new_name)
    return 0
