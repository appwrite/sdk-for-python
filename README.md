# Appwrite Python SDK

![License](https://img.shields.io/badge/license-BSD--3--Clause-blue.svg?style=flat-square)
![Version](https://img.shields.io/badge/api%20version-2.5.0-blue.svg?style=flat-square)
[![X Account](https://img.shields.io/badge/follow-%40appwrite-000000?logo=x&style=flat-square)](https://x.com/appwrite)
[![Discord](https://img.shields.io/discord/564160730845151244?label=discord&style=flat-square)](https://appwrite.io/discord)

**This SDK targets Appwrite server version 2.5.x as shipped on Appwrite Cloud.** Self-hosted releases can lag behind Cloud — if you run an older self-hosted build, use a matching older SDK from [previous releases](https://github.com/appwrite/sdk-for-python/releases) when APIs differ.

Appwrite is an open-source backend as a service server that abstracts and simplifies complex and repetitive development tasks behind a very simple to use REST API. Appwrite aims to help you develop your apps faster and in a more secure way. Use the Python SDK to integrate your app with the Appwrite server to easily start interacting with all of Appwrite backend APIs and tools. For full API documentation and tutorials go to [https://appwrite.io/docs](https://appwrite.io/docs)

![Appwrite](https://github.com/appwrite/appwrite/raw/main/public/images/github.png)

## Installation

Requires Python 3.11 or later. Install the [`appwrite`](https://pypi.org/project/appwrite/) package from PyPI:

```bash
pip install appwrite
```

Or with [uv](https://docs.astral.sh/uv/):

```bash
uv add appwrite
```

## Getting started

Every API call is asynchronous, so every service method returns a coroutine you `await`.

### Initialize the client

Create a client with your Appwrite endpoint, project ID and an [API key](https://appwrite.io/docs/partners/project/api-keys). Find the endpoint and project ID in your project's **Settings** page, and create an API key with only the scopes you need under **API keys** in the project sidebar.

```python
from appwrite.client import Client

client = Client()
client.set_endpoint('https://<REGION>.cloud.appwrite.io/v1')
client.set_project('<PROJECT_ID>')
client.set_key('<API_KEY>')
```

API keys grant server-level access to your project. Keep them out of client-side code and version control.

### Make a request

Create a service object with the client and await any of its methods. Every method returns a typed Pydantic model, so response fields are available as attributes.

```python
import asyncio

from appwrite.id import ID
from appwrite.services.users import Users


async def main():
    users = Users(client)

    user = await users.create(
        user_id=ID.unique(),
        email='email@example.com',
        password='password',
        name="Walter O'Brien",
    )

    print(user.id)
    print(user.name)
    print(user.to_dict())


asyncio.run(main())
```

See the [API reference](https://appwrite.io/docs/references/cloud/server-python/users) for every service and method.

### Work with rows

Use `TablesDB` to read and write rows. Pass a Pydantic model as `model_type` to get typed row data back; without it, `row.data` is a `dict`.

```python
from typing import Optional

from pydantic import BaseModel

from appwrite.id import ID
from appwrite.query import Query
from appwrite.services.tables_db import TablesDB


class Post(BaseModel):
    title: str
    published: bool
    excerpt: Optional[str] = None


async def main():
    tables_db = TablesDB(client)

    row = await tables_db.create_row(
        database_id='<DATABASE_ID>',
        table_id='<TABLE_ID>',
        row_id=ID.unique(),
        data={'title': 'Hello, world', 'published': True},
        model_type=Post,
    )

    print(row.id)
    print(row.data.title)

    result = await tables_db.list_rows(
        database_id='<DATABASE_ID>',
        table_id='<TABLE_ID>',
        queries=[Query.equal('published', True), Query.limit(25)],
        model_type=Post,
    )

    for row in result.rows:
        print(row.data.title)
```

### Handle errors

Failed requests raise `AppwriteException`, which carries `message`, `code`, `type` and `response`.

```python
from appwrite.exception import AppwriteException

try:
    user = await users.get(user_id='<USER_ID>')
except AppwriteException as error:
    print(error.code, error.type, error.message)
```

### Close the client

The client keeps a pooled HTTP connection open. Close it when you are done, or use it as an async context manager.

```python
await client.aclose()
```

```python
async with Client() as client:
    ...
```

### Self-hosted Appwrite

Point the client at your own instance instead of Appwrite Cloud. Call `set_self_signed()` only in development, when the server uses a self-signed TLS certificate.

```python
client.set_endpoint('https://appwrite.example.com/v1')
client.set_self_signed()
```

### Learn more

- [Python quick start](https://appwrite.io/docs/quick-starts/python)
- [Python API reference](https://appwrite.io/docs/references/cloud/server-python/users)
- [Appwrite docs](https://appwrite.io/docs)
- [Discord community](https://appwrite.io/discord)
- [Appwrite Python playground](https://github.com/appwrite/playground-for-python)

## Contribution

This library is auto-generated by Appwrite custom [SDK Generator](https://github.com/appwrite/sdk-generator). To learn more about how you can help us improve this SDK, please check the [contribution guide](https://github.com/appwrite/sdk-generator/blob/main/CONTRIBUTING.md) before sending a pull-request.

## License

Please see the [BSD-3-Clause license](https://raw.githubusercontent.com/appwrite/appwrite/master/LICENSE) file for more information.
