```python
from appwrite.client import Client
from appwrite.services.videos import Videos
from appwrite.models import VideoRendition

client = Client()
client.set_endpoint('https://<REGION>.cloud.appwrite.io/v1') # Your API Endpoint
client.set_project('<YOUR_PROJECT_ID>') # Your project ID
client.set_session('') # The user session to authenticate with

videos = Videos(client)

result: VideoRendition = videos.get_rendition(
    video_id = '<VIDEO_ID>',
    rendition_id = '<RENDITION_ID>'
)

print(result.model_dump())
```
