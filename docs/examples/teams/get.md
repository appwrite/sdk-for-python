```python
from appwrite.client import Client
from appwrite.services.teams import Teams
from appwrite.models import Team

client = Client()
client.set_endpoint('https://<REGION>.cloud.appwrite.io/v1') # Your API Endpoint
client.set_project('<YOUR_PROJECT_ID>') # Your project ID
client.set_session('') # The user session to authenticate with

teams = Teams(client)

result: Team = teams.get(
    team_id = '<TEAM_ID>'
)

print(result.model_dump())
```
