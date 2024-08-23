"""
This module defines a custom JSON encoder that handles various enum classes.

It provides a convenient way to serialize enum values to their corresponding string representations
when encoding objects to JSON.

Usage:
    import json
    from your_module import ValueClassEncoder

    # Create an instance of the encoder
    encoder = ValueClassEncoder()

    # Serialize an object containing enum values
    json_data = json.dumps(your_object, cls=ValueClassEncoder)
"""
import json
from ..enums.authenticator_type import AuthenticatorType
from ..enums.authentication_factor import AuthenticationFactor
from ..enums.o_auth_provider import OAuthProvider
from ..enums.browser import Browser
from ..enums.credit_card import CreditCard
from ..enums.flag import Flag
from ..enums.relationship_type import RelationshipType
from ..enums.relation_mutate import RelationMutate
from ..enums.index_type import IndexType
from ..enums.runtime import Runtime
from ..enums.execution_method import ExecutionMethod
from ..enums.name import Name
from ..enums.smtp_encryption import SmtpEncryption
from ..enums.compression import Compression
from ..enums.image_gravity import ImageGravity
from ..enums.image_format import ImageFormat
from ..enums.password_hash import PasswordHash
from ..enums.messaging_provider_type import MessagingProviderType


class ValueClassEncoder(json.JSONEncoder):
    """Custom JSON encoder for handling enum classes."""
    
    VALUE_CLASSES = (
        AuthenticatorType,
        AuthenticationFactor,
        OAuthProvider,
        Browser,
        CreditCard,
        Flag,
        RelationshipType,
        RelationMutate,
        IndexType,
        Runtime,
        ExecutionMethod,
        Name,
        SmtpEncryption,
        Compression,
        ImageGravity,
        ImageFormat,
        PasswordHash,
        MessagingProviderType,
    )

    def default(self, o):
        """Encodes the given object to a JSON representation.

        Args:
            o: The object to be encoded.

        Returns:
            The JSON representation of the object.
        """
        for enum_class in self.VALUE_CLASSES:
            if isinstance(o, enum_class):
                return o.value
        return super().default(o)
