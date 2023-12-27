import io
from bitlist import bitlist


def read_bits_from_file(filename: str) -> bitlist:
    """read the bits from a given file in memory"""
    with open(filename, "rb") as f:
        return bitlist(f.read())


def build_file_in_memory_from_bits(content: bitlist) -> io.BytesIO:
    """create a BytesIO object from a given array of bits"""
    file = io.BytesIO(content.to_bytes())
    return file


def write_file_to_disk(file: io.BytesIO, filename: str) -> None:
    """Write a BytesIO file to disk"""
    with open(filename, "wb") as f:
        f.write(file.getbuffer())
