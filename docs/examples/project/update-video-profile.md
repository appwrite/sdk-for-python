```python
from appwrite.client import Client
from appwrite.services.project import Project
from appwrite.models import VideoProfile

client = Client()
client.set_endpoint('https://<REGION>.cloud.appwrite.io/v1') # Your API Endpoint
client.set_project('<YOUR_PROJECT_ID>') # Your project ID
client.set_key('<YOUR_API_KEY>') # Your secret API key

project = Project(client)

result: VideoProfile = project.update_video_profile(
    profile_id = '<PROFILE_ID>',
    name = '<NAME>', # optional
    video_bit_rate = 32000, # optional
    audio_bit_rate = 32000, # optional
    width = 16, # optional
    height = 16 # optional
)

print(result.model_dump())
```
