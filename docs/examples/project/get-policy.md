```python
import asyncio

from appwrite.client import Client
from appwrite.services.project import Project
from appwrite.models import PolicyPasswordDictionary
from appwrite.models import PolicyPasswordHistory
from appwrite.models import PolicyPasswordStrength
from appwrite.models import PolicyPasswordPersonalData
from appwrite.models import PolicyPasswordPwned
from appwrite.models import PolicyPasswordRotation
from appwrite.models import PolicySessionAlert
from appwrite.models import PolicySessionDuration
from appwrite.models import PolicySessionInvalidation
from appwrite.models import PolicySessionLimit
from appwrite.models import PolicyUserLimit
from appwrite.models import PolicyMembershipPrivacy
from appwrite.models import PolicyMfaFactors
from appwrite.models import PolicyDenyAliasedEmail
from appwrite.models import PolicyDenyDisposableEmail
from appwrite.models import PolicyDenyFreeEmail
from appwrite.models import PolicyDenyCorporateEmail
from appwrite.models import PolicyPasskey
from typing import Union
from appwrite.enums.project_policy_id import ProjectPolicyId


async def main():
    client = Client()
    client.set_endpoint('https://<REGION>.cloud.appwrite.io/v1') # Your API Endpoint
    client.set_project('<YOUR_PROJECT_ID>') # Your project ID
    client.set_key('<YOUR_API_KEY>') # Your secret API key

    project = Project(client)

    result: Union[PolicyPasswordDictionary, PolicyPasswordHistory, PolicyPasswordStrength, PolicyPasswordPersonalData, PolicyPasswordPwned, PolicyPasswordRotation, PolicySessionAlert, PolicySessionDuration, PolicySessionInvalidation, PolicySessionLimit, PolicyUserLimit, PolicyMembershipPrivacy, PolicyMfaFactors, PolicyDenyAliasedEmail, PolicyDenyDisposableEmail, PolicyDenyFreeEmail, PolicyDenyCorporateEmail, PolicyPasskey] = await project.get_policy(
        policy_id = ProjectPolicyId.PASSWORD_DICTIONARY
    )

    print(result.model_dump())


asyncio.run(main())
```
