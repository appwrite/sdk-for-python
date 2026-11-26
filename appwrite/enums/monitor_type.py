from enum import Enum


class MonitorType(Enum):
    USAGE = "usage"
    HTTP = "http"
    DNS = "dns"
    TCP = "tcp"
    SMTP = "smtp"
    BUDGET = "budget"
