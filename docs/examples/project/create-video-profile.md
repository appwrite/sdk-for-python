```python
from appwrite.client import Client
from appwrite.services.project import Project
from appwrite.models import VideoProfile
from appwrite.enums.video_codec_id import VideoCodecId

client = Client()
client.set_endpoint('https://<REGION>.cloud.appwrite.io/v1') # Your API Endpoint
client.set_project('<YOUR_PROJECT_ID>') # Your project ID
client.set_key('<YOUR_API_KEY>') # Your secret API key

project = Project(client)

result: VideoProfile = project.create_video_profile(
    profile_id = '<PROFILE_ID>',
    name = '<NAME>',
    video_bit_rate = 32000,
    audio_bit_rate = 32000,
    width = 16,
    height = 16,
    codec = VideoCodecId.H264 # optional
)

print(result.model_dump())
```
