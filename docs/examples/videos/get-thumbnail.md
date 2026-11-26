```python
from appwrite.client import Client
from appwrite.services.videos import Videos
from appwrite.enums.image_format import ImageFormat

client = Client()
client.set_endpoint('https://<REGION>.cloud.appwrite.io/v1') # Your API Endpoint
client.set_project('<YOUR_PROJECT_ID>') # Your project ID
client.set_session('') # The user session to authenticate with

videos = Videos(client)

result: bytes = videos.get_thumbnail(
    video_id = '<VIDEO_ID>',
    thumbnail_id = '<THUMBNAIL_ID>',
    width = 0, # optional
    height = 0, # optional
    output = ImageFormat.JPG # optional
)
```
