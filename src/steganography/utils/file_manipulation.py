import io
from bitlist import bitlist


def read_bits_from_file(filename: str) -> bitlist:
    with open(filename, "rb") as f:
        return bitlist(f.read())


def build_file_in_memory_from_bits(content: bitlist) -> io.BytesIO:
    file = io.BytesIO(content.to_bytes())
    return file


def write_file_to_disk(file: io.BytesIO, filename: str) -> None:
    with open(filename, "wb") as f:
        f.write(file.getbuffer())
