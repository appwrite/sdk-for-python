from enum import Enum


class MonitorTlsMode(Enum):
    NONE = "none"
    STARTTLS = "starttls"
    IMPLICIT = "implicit"
    AUTO = "auto"
