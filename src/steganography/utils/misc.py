from typing import Callable

__all__ = ["HashFunction"]

HashFunction = Callable[[bytes], str]
