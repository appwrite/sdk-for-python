from typing import Any, Dict, List, Optional, Union, cast, Generic, TypeVar, Type
from pydantic import Field, PrivateAttr, model_validator

from .base_model import AppwriteModel
from .algo_argon2 import AlgoArgon2
from .algo_scrypt import AlgoScrypt
from .algo_scrypt_modified import AlgoScryptModified
from .algo_bcrypt import AlgoBcrypt
from .algo_phpass import AlgoPhpass
from .algo_sha import AlgoSha
from .algo_md5 import AlgoMd5
from .preferences import Preferences
from .target import Target

T = TypeVar('T')


class User(AppwriteModel, Generic[T]):
    """
    User

    Attributes
    ----------
    id : str
        User ID.
    createdat : str
        User creation date in ISO 8601 format.
    updatedat : str
        User update date in ISO 8601 format.
    name : str
        User name.
    password : Optional[str]
        Hashed user password.
    hash : Optional[str]
        Password hashing algorithm.
    hashoptions : Optional[Union[AlgoArgon2, AlgoScrypt, AlgoScryptModified, AlgoBcrypt, AlgoPhpass, AlgoSha, AlgoMd5]]
        Password hashing algorithm configuration.
    registration : str
        User registration date in ISO 8601 format.
    status : bool
        User status. Pass `true` for enabled and `false` for disabled.
    labels : List[Any]
        Labels for the user.
    passwordupdate : str
        Password update time in ISO 8601 format.
    email : str
        User email address.
    phone : str
        User phone number in E.164 format.
    emailverification : bool
        Email verification status.
    emailcanonical : Optional[str]
        Canonical form of the user email address.
    emailisfree : Optional[bool]
        Whether the user email is from a free email provider.
    emailisdisposable : Optional[bool]
        Whether the user email is from a disposable email provider.
    emailiscorporate : Optional[bool]
        Whether the user email is from a corporate domain.
    emailiscanonical : Optional[bool]
        Whether the user email is in its canonical form.
    passwordpwned : Optional[bool]
        Whether the password was found in a known data breach the last time it was checked. Null when the password has never been checked.
    phoneverification : bool
        Phone verification status.
    mfa : bool
        Multi factor authentication status.
    prefs : Preferences[T]
        User preferences as a key-value object
    targets : List[Target]
        A user-owned message receiver. A single user may have multiple e.g. emails, phones, and a browser. Each target is registered with a single provider.
    accessedat : str
        Most recent access date in ISO 8601 format. This attribute is only updated again after 24 hours.
    impersonator : Optional[bool]
        Whether the user can impersonate other users.
    impersonatoruserid : Optional[str]
        ID of the original actor performing the impersonation. Present only when the current request is impersonating another user. Internal audit logs attribute the action to this user, while the impersonated target is recorded only in internal audit payload data.
    """

    id: str = Field(..., alias='$id')
    createdat: str = Field(..., alias='$createdAt')
    updatedat: str = Field(..., alias='$updatedAt')
    name: str = Field(..., alias='name')
    password: Optional[str] = Field(default=None, alias='password')
    hash: Optional[str] = Field(default=None, alias='hash')
    hashoptions: Optional[
        Union[
            AlgoArgon2,
            AlgoScrypt,
            AlgoScryptModified,
            AlgoBcrypt,
            AlgoPhpass,
            AlgoSha,
            AlgoMd5,
        ]
    ] = Field(default=None, alias='hashOptions')
    registration: str = Field(..., alias='registration')
    status: bool = Field(..., alias='status')
    labels: List[Any] = Field(..., alias='labels')
    passwordupdate: str = Field(..., alias='passwordUpdate')
    email: str = Field(..., alias='email')
    phone: str = Field(..., alias='phone')
    emailverification: bool = Field(..., alias='emailVerification')
    emailcanonical: Optional[str] = Field(default=None, alias='emailCanonical')
    emailisfree: Optional[bool] = Field(default=None, alias='emailIsFree')
    emailisdisposable: Optional[bool] = Field(default=None, alias='emailIsDisposable')
    emailiscorporate: Optional[bool] = Field(default=None, alias='emailIsCorporate')
    emailiscanonical: Optional[bool] = Field(default=None, alias='emailIsCanonical')
    passwordpwned: Optional[bool] = Field(default=None, alias='passwordPwned')
    phoneverification: bool = Field(..., alias='phoneVerification')
    mfa: bool = Field(..., alias='mfa')
    prefs: Preferences[T] = Field(..., alias='prefs')
    targets: List[Target] = Field(..., alias='targets')
    accessedat: str = Field(..., alias='accessedAt')
    impersonator: Optional[bool] = Field(default=None, alias='impersonator')
    impersonatoruserid: Optional[str] = Field(default=None, alias='impersonatorUserId')

    @model_validator(mode='before')
    @classmethod
    def _apply_defaults(cls, data: Any) -> Any:
        if not isinstance(data, dict):
            return data

        data = dict(data)
        if '$id' not in data and 'id' not in data:
            data['$id'] = ''
        if '$createdAt' not in data and 'createdat' not in data:
            data['$createdAt'] = ''
        if '$updatedAt' not in data and 'updatedat' not in data:
            data['$updatedAt'] = ''
        if 'name' not in data:
            data['name'] = ''
        if 'registration' not in data:
            data['registration'] = ''
        if 'status' not in data:
            data['status'] = True
        if 'labels' not in data:
            data['labels'] = []
        if 'passwordUpdate' not in data and 'passwordupdate' not in data:
            data['passwordUpdate'] = ''
        if 'email' not in data:
            data['email'] = ''
        if 'phone' not in data:
            data['phone'] = ''
        if 'emailVerification' not in data and 'emailverification' not in data:
            data['emailVerification'] = False
        if 'phoneVerification' not in data and 'phoneverification' not in data:
            data['phoneVerification'] = False
        if 'mfa' not in data:
            data['mfa'] = False
        if 'accessedAt' not in data and 'accessedat' not in data:
            data['accessedAt'] = ''
        return data

    @classmethod
    def with_data(cls, data: Dict[str, Any], model_type: Type[T] = dict) -> 'User[T]':
        """Create User instance with typed data."""
        instance = cls.model_validate(data)
        if 'prefs' in data and data['prefs'] is not None:
            instance.prefs = Preferences.with_data(data['prefs'], model_type)
        return instance
