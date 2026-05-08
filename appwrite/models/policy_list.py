from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from .policy_password_dictionary import PolicyPasswordDictionary
from .policy_password_history import PolicyPasswordHistory
from .policy_password_personal_data import PolicyPasswordPersonalData
from .policy_session_alert import PolicySessionAlert
from .policy_session_duration import PolicySessionDuration
from .policy_session_invalidation import PolicySessionInvalidation
from .policy_session_limit import PolicySessionLimit
from .policy_user_limit import PolicyUserLimit
from .policy_membership_privacy import PolicyMembershipPrivacy

class PolicyList(AppwriteModel):
    """
    Policies List

    Attributes
    ----------
    total : float
        Total number of policies in the given project.
    policies : List[Union[PolicyPasswordDictionary, PolicyPasswordHistory, PolicyPasswordPersonalData, PolicySessionAlert, PolicySessionDuration, PolicySessionInvalidation, PolicySessionLimit, PolicyUserLimit, PolicyMembershipPrivacy]]
        List of policies.
    """
    total: float = Field(..., alias='total')
    policies: List[Union[PolicyPasswordDictionary, PolicyPasswordHistory, PolicyPasswordPersonalData, PolicySessionAlert, PolicySessionDuration, PolicySessionInvalidation, PolicySessionLimit, PolicyUserLimit, PolicyMembershipPrivacy]] = Field(..., alias='policies')
