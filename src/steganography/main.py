from __future__ import annotations
from steganography.decode import decode_file_from_image
from steganography.encode import encode_file_in_image
from typing import Optional, Sequence
from argparse import ArgumentParser
from pathlib import Path
from PIL import Image


def _init_argparser() -> ArgumentParser:
    parser = ArgumentParser(prog="steganography")
    subparsers = parser.add_subparsers(required=True, dest="mode")
    embed = subparsers.add_parser("embed", help="Embeding", aliases=["em"])
    extract = subparsers.add_parser("extract", help="Extracting", aliases=["ex"])
    embed.add_argument(
        "-t", "--target", required=True, type=Path, help="Pfad der target Datei"
    )
    embed.add_argument(
        "-p", "--payload", required=True, type=Path, help="Pfad der payload Datei"
    )
    extract.add_argument("file", type=Path, help="File with the hidden connent")
    embed.add_argument(
        "--password", type=str, help="Passwort zum verschlüsseln der Datei"
    )
    embed.add_argument(
        "-b",
        "--lsb",
        default=1,
        type=int,
        choices=range(1, 9),
        help="Die Anzahl an LSB's die überschrieben werden",
    )
    embed.add_argument(
        "-o", "--output", type=Path, default=None, help="Pfad der output Datei"
    )
    extract.add_argument(
        "--password", type=str, help="Passwort mit der die Datei verschlüsselt wurde"
    )
    extract.add_argument(
        "--no-hash",
        action="store_true",
        help="Der Hash der Datei wurde nicht eingebettet",
    )
    embed.add_argument(
        "--no-hash", action="store_true", help="Der Hash der Datei nicht einbetten"
    )

    return parser


def main(*argv: str) -> int:
    parser = _init_argparser()
    args = parser.parse_args(argv or None)
    if args.mode in ("embed", "em"):
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
    if args.mode in ("extract", "ex"):
        image_path = args.file
        encryption_key = args.password
        hashing = not args.no_hash
        image = Image.open(image_path)

        file_name, file_bytes = decode_file_from_image(image, encryption_key, hashing)
        with open(file_name, "wb") as f:
            f.write(file_bytes)
    return 0


if __name__ == "__main__":
    #  raise SystemExit(main("extract", "-h"))
    raise SystemExit(main("embed", "-t", "asdf", "-p", "adf"))
