from enum import Enum


class ProjectLDAPEncryption(Enum):
    NONE = "none"
    LDAPS = "ldaps"
    STARTTLS = "starttls"
