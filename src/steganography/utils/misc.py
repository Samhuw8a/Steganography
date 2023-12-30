from typing import Callable, Any


HashFunction = Callable[[bytes], str]


class ImageTypeException(TypeError):
    pass


class ImageModeException(TypeError):
    pass
