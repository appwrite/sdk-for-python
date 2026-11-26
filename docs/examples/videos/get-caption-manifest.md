```python
from appwrite.client import Client
from appwrite.services.videos import Videos
from appwrite.enums.video_output import VideoOutput

client = Client()
client.set_endpoint('https://<REGION>.cloud.appwrite.io/v1') # Your API Endpoint
client.set_project('<YOUR_PROJECT_ID>') # Your project ID
client.set_session('') # The user session to authenticate with

videos = Videos(client)

result: bytes = videos.get_caption_manifest(
    video_id = '<VIDEO_ID>',
    output = VideoOutput.HLS,
    caption_id = '<CAPTION_ID>'
)
```
