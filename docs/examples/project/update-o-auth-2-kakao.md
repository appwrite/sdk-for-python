```python
import asyncio

from appwrite.client import Client
from appwrite.services.project import Project
from appwrite.models import OAuth2Kakao
from appwrite.enums.project_o_auth2_kakao_prompt import ProjectOAuth2KakaoPrompt


async def main():
    client = Client()
    client.set_endpoint('https://<REGION>.cloud.appwrite.io/v1') # Your API Endpoint
    client.set_project('<YOUR_PROJECT_ID>') # Your project ID
    client.set_key('<YOUR_API_KEY>') # Your secret API key

    project = Project(client)

    result: OAuth2Kakao = await project.update_o_auth2_kakao(
        client_id = '<CLIENT_ID>', # optional
        client_secret = '<CLIENT_SECRET>', # optional
        enabled = False, # optional
        prompt = [ProjectOAuth2KakaoPrompt.NONE] # optional
    )

    print(result.model_dump())


asyncio.run(main())
```
