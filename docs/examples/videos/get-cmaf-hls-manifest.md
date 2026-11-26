```python
from appwrite.client import Client
from appwrite.services.videos import Videos

client = Client()
client.set_endpoint('https://<REGION>.cloud.appwrite.io/v1') # Your API Endpoint
client.set_project('<YOUR_PROJECT_ID>') # Your project ID
client.set_session('') # The user session to authenticate with

videos = Videos(client)

result: bytes = videos.get_cmaf_hls_manifest(
    video_id = '<VIDEO_ID>'
)
```
