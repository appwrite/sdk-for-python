```python
from appwrite.client import Client
from appwrite.services.teams import Teams
from appwrite.input_file import InputFile
from appwrite.models import Team

client = Client()
client.set_endpoint('https://<REGION>.cloud.appwrite.io/v1') # Your API Endpoint
client.set_project('<YOUR_PROJECT_ID>') # Your project ID
client.set_session('') # The user session to authenticate with

teams = Teams(client)

result: Team = teams.update_photo(
    team_id = '<TEAM_ID>',
    file = InputFile.from_path('file.png')
)

print(result.model_dump())
```
