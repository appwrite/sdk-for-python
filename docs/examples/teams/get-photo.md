```python
from appwrite.client import Client
from appwrite.services.teams import Teams

client = Client()
client.set_endpoint('https://<REGION>.cloud.appwrite.io/v1') # Your API Endpoint
client.set_project('<YOUR_PROJECT_ID>') # Your project ID
client.set_session('') # The user session to authenticate with

teams = Teams(client)

result: bytes = teams.get_photo(
    team_id = '<TEAM_ID>',
    width = 0, # optional
    height = 0, # optional
    quality = 0, # optional
    output = 'png' # optional
)
```
