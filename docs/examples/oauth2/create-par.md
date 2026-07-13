```python
from appwrite.client import Client
from appwrite.services.oauth2 import Oauth2
from appwrite.models import Oauth2PAR

client = Client()
client.set_endpoint('https://<REGION>.cloud.appwrite.io/v1') # Your API Endpoint
client.set_session('') # The user session to authenticate with
client.set_project('<YOUR_PROJECT_ID>') # Your project ID

oauth2 = Oauth2(client)

result: Oauth2PAR = oauth2.create_par(
    client_id = '<CLIENT_ID>',
    redirect_uri = 'https://example.com',
    response_type = 'code',
    scope = '<SCOPE>', # optional
    state = '<STATE>', # optional
    nonce = '<NONCE>', # optional
    code_challenge = '<CODE_CHALLENGE>', # optional
    code_challenge_method = 's256', # optional
    prompt = '<PROMPT>', # optional
    max_age = 0, # optional
    authorization_details = '<AUTHORIZATION_DETAILS>', # optional
    resource = '', # optional
    audience = '<AUDIENCE>' # optional
)

print(result.model_dump())
```
