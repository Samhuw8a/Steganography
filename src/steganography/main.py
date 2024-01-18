from typing import Optional, Sequence
from argparse import ArgumentParser
from pathlib import Path


def _init_argparser() -> ArgumentParser:
    parser = ArgumentParser(prog="steganography")
    subparsers = parser.add_subparsers(required=True)
    embed = subparsers.add_parser("embed", help="Embeding")
    extract = subparsers.add_parser("extract", help="Extracting")
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
    print(args)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
