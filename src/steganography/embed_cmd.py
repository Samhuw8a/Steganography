from __future__ import annotations

from argparse import Namespace
from pathlib import Path

from PIL import Image, UnidentifiedImageError

from steganography.encode import encode_file_in_image


def image_is_valid(path: str):
    """Helper for checking if an Image exists"""
    try:
        f = Path(path)
    except Exception:
        return False
    if not f.suffix == ".png":
        return False
    return True


def embed(args: Namespace) -> int:
    image_path = args.target
    # Check if the Image, which the User provided is valid
    if not image_path.exists():
        raise FileNotFoundError(f"The image {image_path} does not exist")
    file = args.payload
    # Check if the File, which the User provided exists
    if not file.exists():
        raise FileNotFoundError(f"The file {file} does not exist")
    # Load all nescecary Vars from  args
    file_name = file.name
    n_lsb = args.lsb
    hashing = not args.no_hash
    encryption_key = args.password
    new_name = image_path.name
    if args.output is not None:
        # Check if the user provided out name is valid
        # If there is no out name, no validation is needed
        if not image_is_valid(args.output):
            raise FileNotFoundError(f"{args.output} is not a valid image format")
        new_name = args.output
    try:
        image = Image.open(image_path)
    except UnidentifiedImageError:
        # Raise Error if the Image cant be opened
        raise FileNotFoundError(f"{image_path} is not a valid Image")

    with file.open("rb") as f:
        # Read the bytes from the target file
        file_bytes = f.read()
        # Run the main encoding algorithm
        new_image = encode_file_in_image(
            file_bytes, file_name, image, n_lsb, encryption_key, hashing
        )
        # Save the Modified Image
        new_image.save(new_name)
    return 0
