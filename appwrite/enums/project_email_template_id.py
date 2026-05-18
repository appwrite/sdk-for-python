from enum import Enum

class ProjectEmailTemplateId(Enum):
    VERIFICATION = "verification"
    MAGICSESSION = "magicSession"
    RECOVERY = "recovery"
    INVITATION = "invitation"
    MFACHALLENGE = "mfaChallenge"
    SESSIONALERT = "sessionAlert"
    OTPSESSION = "otpSession"
