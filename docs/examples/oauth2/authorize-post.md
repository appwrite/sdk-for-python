```python
from appwrite.client import Client
from appwrite.services.oauth2 import Oauth2
from appwrite.models import Oauth2Authorize

client = Client()
client.set_endpoint('https://<REGION>.cloud.appwrite.io/v1') # Your API Endpoint
client.set_session('') # The user session to authenticate with
client.set_project('<YOUR_PROJECT_ID>') # Your project ID

oauth2 = Oauth2(client)

result: Oauth2Authorize = oauth2.authorize_post(
    client_id = '<CLIENT_ID>', # optional
    redirect_uri = 'https://example.com', # optional
    response_type = '', # optional
    scope = '<SCOPE>', # optional
    state = '<STATE>', # optional
    nonce = '<NONCE>', # optional
    code_challenge = '<CODE_CHALLENGE>', # optional
    code_challenge_method = 's256', # optional
    prompt = '<PROMPT>', # optional
    max_age = 0, # optional
    authorization_details = '<AUTHORIZATION_DETAILS>', # optional
    resource = '', # optional
    audience = '<AUDIENCE>', # optional
    request_uri = '<REQUEST_URI>' # optional
)

print(result.model_dump())
```
