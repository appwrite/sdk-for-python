from enum import Enum

class Compression(Enum):
    NONE = "none"
    GZIP = "gzip"
    ZSTD = "zstd"
