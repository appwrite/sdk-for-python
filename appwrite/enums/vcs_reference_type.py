from enum import Enum

class VCSReferenceType(Enum):
    BRANCH = "branch"
    COMMIT = "commit"
    TAG = "tag"
