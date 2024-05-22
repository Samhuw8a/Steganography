from __future__ import annotations
import sys
from PIL import Image


def main() -> int:
    args = sys.argv
    assert len(args) == 2
    image = Image.open(args[1])
    print(f"size: {image.size}")
    print(f"mode: {image.mode}")

    inp = input("Convert to: ")
    if not inp:
        print("No conversion")
    else:
        new = image.convert(inp.upper())
        new.save(args[1][:-4] + ".out" + args[1][-4:])
        print("saved to new image")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
