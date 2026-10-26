```python
import asyncio

from appwrite.client import Client
from appwrite.services.project import Project
from appwrite.models import OAuth2Salesforce
from appwrite.enums.project_o_auth2_salesforce_prompt import ProjectOAuth2SalesforcePrompt


async def main():
    client = Client()
    client.set_endpoint('https://<REGION>.cloud.appwrite.io/v1') # Your API Endpoint
    client.set_project('<YOUR_PROJECT_ID>') # Your project ID
    client.set_key('<YOUR_API_KEY>') # Your secret API key

    project = Project(client)

    result: OAuth2Salesforce = await project.update_o_auth2_salesforce(
        customer_key = '<CUSTOMER_KEY>', # optional
        customer_secret = '<CUSTOMER_SECRET>', # optional
        enabled = False, # optional
        prompt = [ProjectOAuth2SalesforcePrompt.LOGIN] # optional
    )

    print(result.model_dump())


asyncio.run(main())
```
