```python
from appwrite.client import Client
from appwrite.services.videos import Videos
from appwrite.models import VideoRendition
from appwrite.enums.video_output import VideoOutput

client = Client()
client.set_endpoint('https://<REGION>.cloud.appwrite.io/v1') # Your API Endpoint
client.set_project('<YOUR_PROJECT_ID>') # Your project ID
client.set_key('<YOUR_API_KEY>') # Your secret API key

videos = Videos(client)

result: VideoRendition = videos.create_rendition(
    video_id = '<VIDEO_ID>',
    profile_id = '<PROFILE_ID>',
    output = VideoOutput.HLS
)

print(result.model_dump())
```
