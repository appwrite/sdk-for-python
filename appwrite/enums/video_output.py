from enum import Enum


class VideoOutput(Enum):
    HLS = "hls"
    DASH = "dash"
    CMAF = "cmaf"
