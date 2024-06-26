from __future__ import annotations

from argparse import ArgumentParser
from pathlib import Path
from steganography._logging import logger, non_verbal_conf, debug_conf, no_conf

from steganography.embed_cmd import embed
from steganography.extract_cmd import extract
from steganography.utils.misc import ImageModeError, ImageTypeError, ExtractionError


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
    extract.add_argument("-v", action="store_true", help="print additional info")
    embed.add_argument("-v", action="store_true", help="print additional info")
    extract.add_argument("-d", action="store_true", help="print debug information")
    embed.add_argument("-d", action="store_true", help="print debug information")
    extract.add_argument("-q", action="store_true", help="print no information")
    embed.add_argument("-q", action="store_true", help="print no information")

    return parser


def main(*argv: str) -> int:
    logger.debug("initialising the ArgumentParser")
    parser = _init_argparser()
    logger.debug("parsing the CLI Arguments")
    args = parser.parse_args(argv or None)
    if not args.v:
        non_verbal_conf()
    if args.d:
        debug_conf()
    if args.q:
        no_conf()

    if args.mode in ("embed", "em"):
        try:
            # Run the embeding Process
            logger.info("Starting the embeding Process")
            return embed(args)
        except (FileNotFoundError, ImageTypeError, ImageModeError) as e:
            # Check for any known/expected Errors and give the user feedback
            logger.warning(e)
            logger.debug("Exit with statuscode 1")
            return 1
    if args.mode in ("extract", "ex"):
        try:
            # Run the exctraction Process
            logger.info("Starting the Extracting Process")
            return extract(args)
        except (
            FileNotFoundError,
            ImageTypeError,
            ImageModeError,
            ExtractionError,
        ) as e:
            # Check for any known/expected Errors and give the user feedback
            # print(e)
            logger.warning(e)
            logger.debug("Exit with statuscode 1")
            return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
