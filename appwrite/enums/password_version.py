from enum import Enum

class PasswordVersion(Enum):
    SHA1 = "sha1"
    SHA224 = "sha224"
    SHA256 = "sha256"
    SHA384 = "sha384"
    SHA512/224 = "sha512/224"
    SHA512/256 = "sha512/256"
    SHA512 = "sha512"
    SHA3224 = "sha3-224"
    SHA3256 = "sha3-256"
    SHA3384 = "sha3-384"
    SHA3512 = "sha3-512"
