```python
from appwrite.client import Client
from appwrite.services.videos import Videos
from appwrite.models import Video
from appwrite.permission import Permission
from appwrite.role import Role

client = Client()
client.set_endpoint('https://<REGION>.cloud.appwrite.io/v1') # Your API Endpoint
client.set_project('<YOUR_PROJECT_ID>') # Your project ID
client.set_session('') # The user session to authenticate with

videos = Videos(client)

result: Video = videos.update(
    video_id = '<VIDEO_ID>',
    name = '<NAME>', # optional
    permissions = [Permission.read(Role.any())] # optional
)

print(result.model_dump())
```
