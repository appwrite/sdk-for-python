from enum import Enum

class VCSDeploymentType(Enum):
    BRANCH = "branch"
    COMMIT = "commit"
    TAG = "tag"
