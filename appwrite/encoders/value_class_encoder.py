import json
from ..enums.authenticator_provider import AuthenticatorProvider
from ..enums.authenticator_factor import AuthenticatorFactor
from ..enums.o_auth_provider import OAuthProvider
from ..enums.browser import Browser
from ..enums.credit_card import CreditCard
from ..enums.flag import Flag
from ..enums.relationship_type import RelationshipType
from ..enums.relation_mutate import RelationMutate
from ..enums.index_type import IndexType
from ..enums.runtime import Runtime
from ..enums.execution_method import ExecutionMethod
from ..enums.message_type import MessageType
from ..enums.smtp_encryption import SMTPEncryption
from ..enums.compression import Compression
from ..enums.image_gravity import ImageGravity
from ..enums.image_format import ImageFormat
from ..enums.password_version import PasswordVersion
from ..enums.messaging_provider_type import MessagingProviderType

class ValueClassEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, AuthenticatorProvider):
            return o.value

        if isinstance(o, AuthenticatorFactor):
            return o.value

        if isinstance(o, OAuthProvider):
            return o.value

        if isinstance(o, Browser):
            return o.value

        if isinstance(o, CreditCard):
            return o.value

        if isinstance(o, Flag):
            return o.value

        if isinstance(o, RelationshipType):
            return o.value

        if isinstance(o, RelationMutate):
            return o.value

        if isinstance(o, IndexType):
            return o.value

        if isinstance(o, Runtime):
            return o.value

        if isinstance(o, ExecutionMethod):
            return o.value

        if isinstance(o, MessageType):
            return o.value

        if isinstance(o, SMTPEncryption):
            return o.value

        if isinstance(o, Compression):
            return o.value

        if isinstance(o, ImageGravity):
            return o.value

        if isinstance(o, ImageFormat):
            return o.value

        if isinstance(o, PasswordVersion):
            return o.value

        if isinstance(o, MessagingProviderType):
            return o.value

        return super().default(o)