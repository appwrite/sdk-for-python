from enum import Enum

class PasswordHash(Enum):
    SHA1 = "sha1"
    SHA224 = "sha224"
    SHA256 = "sha256"
    SHA384 = "sha384"
    SHA512_224 = "sha512/224"
    SHA512_256 = "sha512/256"
    SHA512 = "sha512"
    SHA3_224 = "sha3-224"
    SHA3_256 = "sha3-256"
    SHA3_384 = "sha3-384"
    SHA3_512 = "sha3-512"
