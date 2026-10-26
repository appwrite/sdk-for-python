import json
import httpx2
import respx
import unittest

from appwrite.client import Client
from appwrite.input_file import InputFile
from appwrite.models import *
from appwrite.services.databases import Databases


class DatabasesServiceTest(unittest.IsolatedAsyncioTestCase):

    async def asyncSetUp(self):
        self.client = Client()
        self.databases = Databases(self.client)

    async def asyncTearDown(self):
        await self.client.aclose()

    @respx.mock
    async def test_list(self):
        data = {
            "total": 5.0,
            "databases": [],
        }
        headers = {'Content-Type': 'application/json'}
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.databases.list()
        self.assertEqual(response.to_dict(), data)

    @respx.mock
    async def test_create(self):
        data = {
            "$id": "5e5ea5c16897e",
            "name": "My Database",
            "description": "Customer orders and invoices.",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "enabled": True,
            "type": "legacy",
        }
        headers = {'Content-Type': 'application/json'}
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.databases.create(
            '<DATABASE_ID>',
            '<NAME>',
        )
        self.assertEqual(response.to_dict(), data)

    @respx.mock
    async def test_list_transactions(self):
        data = {
            "total": 5.0,
            "transactions": [],
        }
        headers = {'Content-Type': 'application/json'}
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.databases.list_transactions()
        self.assertEqual(response.to_dict(), data)

    @respx.mock
    async def test_create_transaction(self):
        data = {
            "$id": "259125845563242502",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "status": "pending",
            "operations": 5.0,
            "expiresAt": "2020-10-15T06:38:00.000+00:00",
        }
        headers = {'Content-Type': 'application/json'}
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.databases.create_transaction()
        self.assertEqual(response.to_dict(), data)

    @respx.mock
    async def test_get_transaction(self):
        data = {
            "$id": "259125845563242502",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "status": "pending",
            "operations": 5.0,
            "expiresAt": "2020-10-15T06:38:00.000+00:00",
        }
        headers = {'Content-Type': 'application/json'}
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.databases.get_transaction(
            '<TRANSACTION_ID>',
        )
        self.assertEqual(response.to_dict(), data)

    @respx.mock
    async def test_update_transaction(self):
        data = {
            "$id": "259125845563242502",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "status": "pending",
            "operations": 5.0,
            "expiresAt": "2020-10-15T06:38:00.000+00:00",
        }
        headers = {'Content-Type': 'application/json'}
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.databases.update_transaction(
            '<TRANSACTION_ID>',
        )
        self.assertEqual(response.to_dict(), data)

    @respx.mock
    async def test_delete_transaction(self):
        data = ''
        headers = {'Content-Type': 'application/json'}
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.databases.delete_transaction(
            '<TRANSACTION_ID>',
        )
        self.assertEqual(response, data)

    @respx.mock
    async def test_create_operations(self):
        data = {
            "$id": "259125845563242502",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "status": "pending",
            "operations": 5.0,
            "expiresAt": "2020-10-15T06:38:00.000+00:00",
        }
        headers = {'Content-Type': 'application/json'}
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.databases.create_operations(
            '<TRANSACTION_ID>',
        )
        self.assertEqual(response.to_dict(), data)

    @respx.mock
    async def test_get(self):
        data = {
            "$id": "5e5ea5c16897e",
            "name": "My Database",
            "description": "Customer orders and invoices.",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "enabled": True,
            "type": "legacy",
        }
        headers = {'Content-Type': 'application/json'}
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.databases.get(
            '<DATABASE_ID>',
        )
        self.assertEqual(response.to_dict(), data)

    @respx.mock
    async def test_update(self):
        data = {
            "$id": "5e5ea5c16897e",
            "name": "My Database",
            "description": "Customer orders and invoices.",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "enabled": True,
            "type": "legacy",
        }
        headers = {'Content-Type': 'application/json'}
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.databases.update(
            '<DATABASE_ID>',
        )
        self.assertEqual(response.to_dict(), data)

    @respx.mock
    async def test_delete(self):
        data = ''
        headers = {'Content-Type': 'application/json'}
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.databases.delete(
            '<DATABASE_ID>',
        )
        self.assertEqual(response, data)

    @respx.mock
    async def test_list_collections(self):
        data = {
            "total": 5.0,
            "collections": [],
        }
        headers = {'Content-Type': 'application/json'}
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.databases.list_collections(
            '<DATABASE_ID>',
        )
        self.assertEqual(response.to_dict(), data)

    @respx.mock
    async def test_create_collection(self):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "$permissions": [],
            "databaseId": "5e5ea5c16897e",
            "name": "My Collection",
            "description": "Movies available in the catalog.",
            "enabled": True,
            "documentSecurity": True,
            "attributes": [],
            "indexes": [],
            "bytesMax": 65535.0,
            "bytesUsed": 1500.0,
        }
        headers = {'Content-Type': 'application/json'}
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.databases.create_collection(
            '<DATABASE_ID>',
            '<COLLECTION_ID>',
            '<NAME>',
        )
        self.assertEqual(response.to_dict(), data)

    @respx.mock
    async def test_get_collection(self):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "$permissions": [],
            "databaseId": "5e5ea5c16897e",
            "name": "My Collection",
            "description": "Movies available in the catalog.",
            "enabled": True,
            "documentSecurity": True,
            "attributes": [],
            "indexes": [],
            "bytesMax": 65535.0,
            "bytesUsed": 1500.0,
        }
        headers = {'Content-Type': 'application/json'}
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.databases.get_collection(
            '<DATABASE_ID>',
            '<COLLECTION_ID>',
        )
        self.assertEqual(response.to_dict(), data)

    @respx.mock
    async def test_update_collection(self):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "$permissions": [],
            "databaseId": "5e5ea5c16897e",
            "name": "My Collection",
            "description": "Movies available in the catalog.",
            "enabled": True,
            "documentSecurity": True,
            "attributes": [],
            "indexes": [],
            "bytesMax": 65535.0,
            "bytesUsed": 1500.0,
        }
        headers = {'Content-Type': 'application/json'}
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.databases.update_collection(
            '<DATABASE_ID>',
            '<COLLECTION_ID>',
        )
        self.assertEqual(response.to_dict(), data)

    @respx.mock
    async def test_delete_collection(self):
        data = ''
        headers = {'Content-Type': 'application/json'}
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.databases.delete_collection(
            '<DATABASE_ID>',
            '<COLLECTION_ID>',
        )
        self.assertEqual(response, data)

    @respx.mock
    async def test_list_attributes(self):
        data = {
            "total": 5.0,
            "attributes": [],
        }
        headers = {'Content-Type': 'application/json'}
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.databases.list_attributes(
            '<DATABASE_ID>',
            '<COLLECTION_ID>',
        )
        self.assertEqual(response.to_dict(), data)

    @respx.mock
    async def test_create_big_int_attribute(self):
        data = {
            "key": "count",
            "description": "Name shown on the public profile.",
            "type": "bigint",
            "status": "available",
            "error": "string",
            "required": True,
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
        }
        headers = {'Content-Type': 'application/json'}
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.databases.create_big_int_attribute(
            '<DATABASE_ID>',
            '<COLLECTION_ID>',
            '<KEY>',
            True,
        )
        self.assertEqual(response.to_dict(), data)

    @respx.mock
    async def test_update_big_int_attribute(self):
        data = {
            "key": "count",
            "description": "Name shown on the public profile.",
            "type": "bigint",
            "status": "available",
            "error": "string",
            "required": True,
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
        }
        headers = {'Content-Type': 'application/json'}
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.databases.update_big_int_attribute(
            '<DATABASE_ID>',
            '<COLLECTION_ID>',
            '<KEY>',
            True,
            1,
        )
        self.assertEqual(response.to_dict(), data)

    @respx.mock
    async def test_create_boolean_attribute(self):
        data = {
            "key": "isEnabled",
            "description": "Name shown on the public profile.",
            "type": "boolean",
            "status": "available",
            "error": "string",
            "required": True,
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
        }
        headers = {'Content-Type': 'application/json'}
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.databases.create_boolean_attribute(
            '<DATABASE_ID>',
            '<COLLECTION_ID>',
            '<KEY>',
            True,
        )
        self.assertEqual(response.to_dict(), data)

    @respx.mock
    async def test_update_boolean_attribute(self):
        data = {
            "key": "isEnabled",
            "description": "Name shown on the public profile.",
            "type": "boolean",
            "status": "available",
            "error": "string",
            "required": True,
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
        }
        headers = {'Content-Type': 'application/json'}
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.databases.update_boolean_attribute(
            '<DATABASE_ID>',
            '<COLLECTION_ID>',
            '<KEY>',
            True,
            True,
        )
        self.assertEqual(response.to_dict(), data)

    @respx.mock
    async def test_create_datetime_attribute(self):
        data = {
            "key": "birthDay",
            "description": "Name shown on the public profile.",
            "type": "datetime",
            "status": "available",
            "error": "string",
            "required": True,
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "format": "datetime",
        }
        headers = {'Content-Type': 'application/json'}
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.databases.create_datetime_attribute(
            '<DATABASE_ID>',
            '<COLLECTION_ID>',
            '<KEY>',
            True,
        )
        self.assertEqual(response.to_dict(), data)

    @respx.mock
    async def test_update_datetime_attribute(self):
        data = {
            "key": "birthDay",
            "description": "Name shown on the public profile.",
            "type": "datetime",
            "status": "available",
            "error": "string",
            "required": True,
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "format": "datetime",
        }
        headers = {'Content-Type': 'application/json'}
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.databases.update_datetime_attribute(
            '<DATABASE_ID>',
            '<COLLECTION_ID>',
            '<KEY>',
            True,
            '2020-10-15T06:38:00.000+00:00',
        )
        self.assertEqual(response.to_dict(), data)

    @respx.mock
    async def test_create_email_attribute(self):
        data = {
            "key": "userEmail",
            "description": "Name shown on the public profile.",
            "type": "string",
            "status": "available",
            "error": "string",
            "required": True,
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "format": "email",
        }
        headers = {'Content-Type': 'application/json'}
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.databases.create_email_attribute(
            '<DATABASE_ID>',
            '<COLLECTION_ID>',
            '<KEY>',
            True,
        )
        self.assertEqual(response.to_dict(), data)

    @respx.mock
    async def test_update_email_attribute(self):
        data = {
            "key": "userEmail",
            "description": "Name shown on the public profile.",
            "type": "string",
            "status": "available",
            "error": "string",
            "required": True,
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "format": "email",
        }
        headers = {'Content-Type': 'application/json'}
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.databases.update_email_attribute(
            '<DATABASE_ID>',
            '<COLLECTION_ID>',
            '<KEY>',
            True,
            'email@example.com',
        )
        self.assertEqual(response.to_dict(), data)

    @respx.mock
    async def test_create_enum_attribute(self):
        data = {
            "key": "status",
            "description": "Name shown on the public profile.",
            "type": "string",
            "status": "available",
            "error": "string",
            "required": True,
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "elements": [],
            "format": "enum",
        }
        headers = {'Content-Type': 'application/json'}
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.databases.create_enum_attribute(
            '<DATABASE_ID>',
            '<COLLECTION_ID>',
            '<KEY>',
            [],
            True,
        )
        self.assertEqual(response.to_dict(), data)

    @respx.mock
    async def test_update_enum_attribute(self):
        data = {
            "key": "status",
            "description": "Name shown on the public profile.",
            "type": "string",
            "status": "available",
            "error": "string",
            "required": True,
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "elements": [],
            "format": "enum",
        }
        headers = {'Content-Type': 'application/json'}
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.databases.update_enum_attribute(
            '<DATABASE_ID>',
            '<COLLECTION_ID>',
            '<KEY>',
            [],
            True,
            'active',
        )
        self.assertEqual(response.to_dict(), data)

    @respx.mock
    async def test_create_float_attribute(self):
        data = {
            "key": "percentageCompleted",
            "description": "Name shown on the public profile.",
            "type": "double",
            "status": "available",
            "error": "string",
            "required": True,
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
        }
        headers = {'Content-Type': 'application/json'}
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.databases.create_float_attribute(
            '<DATABASE_ID>',
            '<COLLECTION_ID>',
            '<KEY>',
            True,
        )
        self.assertEqual(response.to_dict(), data)

    @respx.mock
    async def test_update_float_attribute(self):
        data = {
            "key": "percentageCompleted",
            "description": "Name shown on the public profile.",
            "type": "double",
            "status": "available",
            "error": "string",
            "required": True,
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
        }
        headers = {'Content-Type': 'application/json'}
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.databases.update_float_attribute(
            '<DATABASE_ID>',
            '<COLLECTION_ID>',
            '<KEY>',
            True,
            1.0,
        )
        self.assertEqual(response.to_dict(), data)

    @respx.mock
    async def test_create_integer_attribute(self):
        data = {
            "key": "count",
            "description": "Name shown on the public profile.",
            "type": "integer",
            "status": "available",
            "error": "string",
            "required": True,
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
        }
        headers = {'Content-Type': 'application/json'}
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.databases.create_integer_attribute(
            '<DATABASE_ID>',
            '<COLLECTION_ID>',
            '<KEY>',
            True,
        )
        self.assertEqual(response.to_dict(), data)

    @respx.mock
    async def test_update_integer_attribute(self):
        data = {
            "key": "count",
            "description": "Name shown on the public profile.",
            "type": "integer",
            "status": "available",
            "error": "string",
            "required": True,
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
        }
        headers = {'Content-Type': 'application/json'}
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.databases.update_integer_attribute(
            '<DATABASE_ID>',
            '<COLLECTION_ID>',
            '<KEY>',
            True,
            1,
        )
        self.assertEqual(response.to_dict(), data)

    @respx.mock
    async def test_create_ip_attribute(self):
        data = {
            "key": "ipAddress",
            "description": "Name shown on the public profile.",
            "type": "string",
            "status": "available",
            "error": "string",
            "required": True,
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "format": "ip",
        }
        headers = {'Content-Type': 'application/json'}
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.databases.create_ip_attribute(
            '<DATABASE_ID>',
            '<COLLECTION_ID>',
            '<KEY>',
            True,
        )
        self.assertEqual(response.to_dict(), data)

    @respx.mock
    async def test_update_ip_attribute(self):
        data = {
            "key": "ipAddress",
            "description": "Name shown on the public profile.",
            "type": "string",
            "status": "available",
            "error": "string",
            "required": True,
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "format": "ip",
        }
        headers = {'Content-Type': 'application/json'}
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.databases.update_ip_attribute(
            '<DATABASE_ID>',
            '<COLLECTION_ID>',
            '<KEY>',
            True,
            '192.0.2.0',
        )
        self.assertEqual(response.to_dict(), data)

    @respx.mock
    async def test_create_line_attribute(self):
        data = {
            "key": "fullName",
            "description": "Name shown on the public profile.",
            "type": "string",
            "status": "available",
            "error": "string",
            "required": True,
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
        }
        headers = {'Content-Type': 'application/json'}
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.databases.create_line_attribute(
            '<DATABASE_ID>',
            '<COLLECTION_ID>',
            '<KEY>',
            True,
        )
        self.assertEqual(response.to_dict(), data)

    @respx.mock
    async def test_update_line_attribute(self):
        data = {
            "key": "fullName",
            "description": "Name shown on the public profile.",
            "type": "string",
            "status": "available",
            "error": "string",
            "required": True,
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
        }
        headers = {'Content-Type': 'application/json'}
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.databases.update_line_attribute(
            '<DATABASE_ID>',
            '<COLLECTION_ID>',
            '<KEY>',
            True,
        )
        self.assertEqual(response.to_dict(), data)

    @respx.mock
    async def test_create_longtext_attribute(self):
        data = {
            "key": "fullName",
            "description": "Name shown on the public profile.",
            "type": "string",
            "status": "available",
            "error": "string",
            "required": True,
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
        }
        headers = {'Content-Type': 'application/json'}
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.databases.create_longtext_attribute(
            '<DATABASE_ID>',
            '<COLLECTION_ID>',
            '<KEY>',
            True,
        )
        self.assertEqual(response.to_dict(), data)

    @respx.mock
    async def test_update_longtext_attribute(self):
        data = {
            "key": "fullName",
            "description": "Name shown on the public profile.",
            "type": "string",
            "status": "available",
            "error": "string",
            "required": True,
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
        }
        headers = {'Content-Type': 'application/json'}
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.databases.update_longtext_attribute(
            '<DATABASE_ID>',
            '<COLLECTION_ID>',
            '<KEY>',
            True,
            'Hello World',
        )
        self.assertEqual(response.to_dict(), data)

    @respx.mock
    async def test_create_mediumtext_attribute(self):
        data = {
            "key": "fullName",
            "description": "Name shown on the public profile.",
            "type": "string",
            "status": "available",
            "error": "string",
            "required": True,
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
        }
        headers = {'Content-Type': 'application/json'}
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.databases.create_mediumtext_attribute(
            '<DATABASE_ID>',
            '<COLLECTION_ID>',
            '<KEY>',
            True,
        )
        self.assertEqual(response.to_dict(), data)

    @respx.mock
    async def test_update_mediumtext_attribute(self):
        data = {
            "key": "fullName",
            "description": "Name shown on the public profile.",
            "type": "string",
            "status": "available",
            "error": "string",
            "required": True,
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
        }
        headers = {'Content-Type': 'application/json'}
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.databases.update_mediumtext_attribute(
            '<DATABASE_ID>',
            '<COLLECTION_ID>',
            '<KEY>',
            True,
            'Hello World',
        )
        self.assertEqual(response.to_dict(), data)

    @respx.mock
    async def test_create_point_attribute(self):
        data = {
            "key": "fullName",
            "description": "Name shown on the public profile.",
            "type": "string",
            "status": "available",
            "error": "string",
            "required": True,
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
        }
        headers = {'Content-Type': 'application/json'}
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.databases.create_point_attribute(
            '<DATABASE_ID>',
            '<COLLECTION_ID>',
            '<KEY>',
            True,
        )
        self.assertEqual(response.to_dict(), data)

    @respx.mock
    async def test_update_point_attribute(self):
        data = {
            "key": "fullName",
            "description": "Name shown on the public profile.",
            "type": "string",
            "status": "available",
            "error": "string",
            "required": True,
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
        }
        headers = {'Content-Type': 'application/json'}
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.databases.update_point_attribute(
            '<DATABASE_ID>',
            '<COLLECTION_ID>',
            '<KEY>',
            True,
        )
        self.assertEqual(response.to_dict(), data)

    @respx.mock
    async def test_create_polygon_attribute(self):
        data = {
            "key": "fullName",
            "description": "Name shown on the public profile.",
            "type": "string",
            "status": "available",
            "error": "string",
            "required": True,
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
        }
        headers = {'Content-Type': 'application/json'}
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.databases.create_polygon_attribute(
            '<DATABASE_ID>',
            '<COLLECTION_ID>',
            '<KEY>',
            True,
        )
        self.assertEqual(response.to_dict(), data)

    @respx.mock
    async def test_update_polygon_attribute(self):
        data = {
            "key": "fullName",
            "description": "Name shown on the public profile.",
            "type": "string",
            "status": "available",
            "error": "string",
            "required": True,
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
        }
        headers = {'Content-Type': 'application/json'}
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.databases.update_polygon_attribute(
            '<DATABASE_ID>',
            '<COLLECTION_ID>',
            '<KEY>',
            True,
        )
        self.assertEqual(response.to_dict(), data)

    @respx.mock
    async def test_create_relationship_attribute(self):
        data = {
            "key": "fullName",
            "description": "Name shown on the public profile.",
            "type": "string",
            "status": "available",
            "error": "string",
            "required": True,
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "relatedCollection": "collection",
            "relationType": "oneToOne|oneToMany|manyToOne|manyToMany",
            "twoWay": True,
            "twoWayKey": "string",
            "onDelete": "restrict|cascade|setNull",
            "side": "parent|child",
        }
        headers = {'Content-Type': 'application/json'}
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.databases.create_relationship_attribute(
            '<DATABASE_ID>',
            '<COLLECTION_ID>',
            '<RELATED_COLLECTION_ID>',
            'oneToOne',
        )
        self.assertEqual(response.to_dict(), data)

    @respx.mock
    async def test_update_relationship_attribute(self):
        data = {
            "key": "fullName",
            "description": "Name shown on the public profile.",
            "type": "string",
            "status": "available",
            "error": "string",
            "required": True,
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "relatedCollection": "collection",
            "relationType": "oneToOne|oneToMany|manyToOne|manyToMany",
            "twoWay": True,
            "twoWayKey": "string",
            "onDelete": "restrict|cascade|setNull",
            "side": "parent|child",
        }
        headers = {'Content-Type': 'application/json'}
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.databases.update_relationship_attribute(
            '<DATABASE_ID>',
            '<COLLECTION_ID>',
            '<KEY>',
        )
        self.assertEqual(response.to_dict(), data)

    @respx.mock
    async def test_create_string_attribute(self):
        data = {
            "key": "fullName",
            "description": "Name shown on the public profile.",
            "type": "string",
            "status": "available",
            "error": "string",
            "required": True,
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "size": 128.0,
        }
        headers = {'Content-Type': 'application/json'}
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.databases.create_string_attribute(
            '<DATABASE_ID>',
            '<COLLECTION_ID>',
            '<KEY>',
            1,
            True,
        )
        self.assertEqual(response.to_dict(), data)

    @respx.mock
    async def test_update_string_attribute(self):
        data = {
            "key": "fullName",
            "description": "Name shown on the public profile.",
            "type": "string",
            "status": "available",
            "error": "string",
            "required": True,
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "size": 128.0,
        }
        headers = {'Content-Type': 'application/json'}
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.databases.update_string_attribute(
            '<DATABASE_ID>',
            '<COLLECTION_ID>',
            '<KEY>',
            True,
            'Hello World',
        )
        self.assertEqual(response.to_dict(), data)

    @respx.mock
    async def test_create_text_attribute(self):
        data = {
            "key": "fullName",
            "description": "Name shown on the public profile.",
            "type": "string",
            "status": "available",
            "error": "string",
            "required": True,
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
        }
        headers = {'Content-Type': 'application/json'}
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.databases.create_text_attribute(
            '<DATABASE_ID>',
            '<COLLECTION_ID>',
            '<KEY>',
            True,
        )
        self.assertEqual(response.to_dict(), data)

    @respx.mock
    async def test_update_text_attribute(self):
        data = {
            "key": "fullName",
            "description": "Name shown on the public profile.",
            "type": "string",
            "status": "available",
            "error": "string",
            "required": True,
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
        }
        headers = {'Content-Type': 'application/json'}
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.databases.update_text_attribute(
            '<DATABASE_ID>',
            '<COLLECTION_ID>',
            '<KEY>',
            True,
            'Hello World',
        )
        self.assertEqual(response.to_dict(), data)

    @respx.mock
    async def test_create_url_attribute(self):
        data = {
            "key": "githubUrl",
            "description": "Name shown on the public profile.",
            "type": "string",
            "status": "available",
            "error": "string",
            "required": True,
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "format": "url",
        }
        headers = {'Content-Type': 'application/json'}
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.databases.create_url_attribute(
            '<DATABASE_ID>',
            '<COLLECTION_ID>',
            '<KEY>',
            True,
        )
        self.assertEqual(response.to_dict(), data)

    @respx.mock
    async def test_update_url_attribute(self):
        data = {
            "key": "githubUrl",
            "description": "Name shown on the public profile.",
            "type": "string",
            "status": "available",
            "error": "string",
            "required": True,
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "format": "url",
        }
        headers = {'Content-Type': 'application/json'}
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.databases.update_url_attribute(
            '<DATABASE_ID>',
            '<COLLECTION_ID>',
            '<KEY>',
            True,
            'https://example.com',
        )
        self.assertEqual(response.to_dict(), data)

    @respx.mock
    async def test_create_varchar_attribute(self):
        data = {
            "key": "fullName",
            "description": "Name shown on the public profile.",
            "type": "string",
            "status": "available",
            "error": "string",
            "required": True,
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "size": 128.0,
        }
        headers = {'Content-Type': 'application/json'}
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.databases.create_varchar_attribute(
            '<DATABASE_ID>',
            '<COLLECTION_ID>',
            '<KEY>',
            1,
            True,
        )
        self.assertEqual(response.to_dict(), data)

    @respx.mock
    async def test_update_varchar_attribute(self):
        data = {
            "key": "fullName",
            "description": "Name shown on the public profile.",
            "type": "string",
            "status": "available",
            "error": "string",
            "required": True,
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "size": 128.0,
        }
        headers = {'Content-Type': 'application/json'}
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.databases.update_varchar_attribute(
            '<DATABASE_ID>',
            '<COLLECTION_ID>',
            '<KEY>',
            True,
            'Hello World',
        )
        self.assertEqual(response.to_dict(), data)

    @respx.mock
    async def test_get_attribute(self):
        data = {
            "key": "isEnabled",
            "description": "Name shown on the public profile.",
            "type": "boolean",
            "status": "available",
            "error": "string",
            "required": True,
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
        }
        headers = {'Content-Type': 'application/json'}
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.databases.get_attribute(
            '<DATABASE_ID>',
            '<COLLECTION_ID>',
            '<KEY>',
        )
        self.assertEqual(response.to_dict(), data)

    @respx.mock
    async def test_delete_attribute(self):
        data = ''
        headers = {'Content-Type': 'application/json'}
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.databases.delete_attribute(
            '<DATABASE_ID>',
            '<COLLECTION_ID>',
            '<KEY>',
        )
        self.assertEqual(response, data)

    @respx.mock
    async def test_list_documents(self):
        data = {
            "total": 5.0,
            "documents": [],
        }
        headers = {'Content-Type': 'application/json'}
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.databases.list_documents(
            '<DATABASE_ID>',
            '<COLLECTION_ID>',
        )
        self.assertEqual(response.to_dict(), data)

    @respx.mock
    async def test_create_document(self):
        data = {
            "$id": "5e5ea5c16897e",
            "$sequence": "1",
            "$collectionId": "5e5ea5c15117e",
            "$databaseId": "5e5ea5c15117e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "$permissions": [],
        }
        headers = {'Content-Type': 'application/json'}
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.databases.create_document(
            '<DATABASE_ID>',
            '<COLLECTION_ID>',
            '<DOCUMENT_ID>',
            {},
        )
        data['data'] = {}
        self.assertEqual(response.to_dict(), data)

    @respx.mock
    async def test_create_documents(self):
        data = {
            "total": 5.0,
            "documents": [],
        }
        headers = {'Content-Type': 'application/json'}
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.databases.create_documents(
            '<DATABASE_ID>',
            '<COLLECTION_ID>',
            [],
        )
        self.assertEqual(response.to_dict(), data)

    @respx.mock
    async def test_upsert_documents(self):
        data = {
            "total": 5.0,
            "documents": [],
        }
        headers = {'Content-Type': 'application/json'}
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.databases.upsert_documents(
            '<DATABASE_ID>',
            '<COLLECTION_ID>',
            [],
        )
        self.assertEqual(response.to_dict(), data)

    @respx.mock
    async def test_update_documents(self):
        data = {
            "total": 5.0,
            "documents": [],
        }
        headers = {'Content-Type': 'application/json'}
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.databases.update_documents(
            '<DATABASE_ID>',
            '<COLLECTION_ID>',
        )
        self.assertEqual(response.to_dict(), data)

    @respx.mock
    async def test_delete_documents(self):
        data = {
            "total": 5.0,
            "documents": [],
        }
        headers = {'Content-Type': 'application/json'}
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.databases.delete_documents(
            '<DATABASE_ID>',
            '<COLLECTION_ID>',
        )
        self.assertEqual(response.to_dict(), data)

    @respx.mock
    async def test_create_query(self):
        data = {
            "total": 5.0,
            "documents": [],
        }
        headers = {'Content-Type': 'application/json'}
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.databases.create_query(
            '<DATABASE_ID>',
            '<COLLECTION_ID>',
        )
        self.assertEqual(response.to_dict(), data)

    @respx.mock
    async def test_get_document(self):
        data = {
            "$id": "5e5ea5c16897e",
            "$sequence": "1",
            "$collectionId": "5e5ea5c15117e",
            "$databaseId": "5e5ea5c15117e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "$permissions": [],
        }
        headers = {'Content-Type': 'application/json'}
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.databases.get_document(
            '<DATABASE_ID>',
            '<COLLECTION_ID>',
            '<DOCUMENT_ID>',
        )
        data['data'] = {}
        self.assertEqual(response.to_dict(), data)

    @respx.mock
    async def test_upsert_document(self):
        data = {
            "$id": "5e5ea5c16897e",
            "$sequence": "1",
            "$collectionId": "5e5ea5c15117e",
            "$databaseId": "5e5ea5c15117e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "$permissions": [],
        }
        headers = {'Content-Type': 'application/json'}
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.databases.upsert_document(
            '<DATABASE_ID>',
            '<COLLECTION_ID>',
            '<DOCUMENT_ID>',
        )
        data['data'] = {}
        self.assertEqual(response.to_dict(), data)

    @respx.mock
    async def test_update_document(self):
        data = {
            "$id": "5e5ea5c16897e",
            "$sequence": "1",
            "$collectionId": "5e5ea5c15117e",
            "$databaseId": "5e5ea5c15117e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "$permissions": [],
        }
        headers = {'Content-Type': 'application/json'}
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.databases.update_document(
            '<DATABASE_ID>',
            '<COLLECTION_ID>',
            '<DOCUMENT_ID>',
        )
        data['data'] = {}
        self.assertEqual(response.to_dict(), data)

    @respx.mock
    async def test_delete_document(self):
        data = ''
        headers = {'Content-Type': 'application/json'}
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.databases.delete_document(
            '<DATABASE_ID>',
            '<COLLECTION_ID>',
            '<DOCUMENT_ID>',
        )
        self.assertEqual(response, data)

    @respx.mock
    async def test_decrement_document_attribute(self):
        data = {
            "$id": "5e5ea5c16897e",
            "$sequence": "1",
            "$collectionId": "5e5ea5c15117e",
            "$databaseId": "5e5ea5c15117e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "$permissions": [],
        }
        headers = {'Content-Type': 'application/json'}
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.databases.decrement_document_attribute(
            '<DATABASE_ID>',
            '<COLLECTION_ID>',
            '<DOCUMENT_ID>',
            '<ATTRIBUTE>',
        )
        data['data'] = {}
        self.assertEqual(response.to_dict(), data)

    @respx.mock
    async def test_increment_document_attribute(self):
        data = {
            "$id": "5e5ea5c16897e",
            "$sequence": "1",
            "$collectionId": "5e5ea5c15117e",
            "$databaseId": "5e5ea5c15117e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "$permissions": [],
        }
        headers = {'Content-Type': 'application/json'}
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.databases.increment_document_attribute(
            '<DATABASE_ID>',
            '<COLLECTION_ID>',
            '<DOCUMENT_ID>',
            '<ATTRIBUTE>',
        )
        data['data'] = {}
        self.assertEqual(response.to_dict(), data)

    @respx.mock
    async def test_list_indexes(self):
        data = {
            "total": 5.0,
            "indexes": [],
        }
        headers = {'Content-Type': 'application/json'}
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.databases.list_indexes(
            '<DATABASE_ID>',
            '<COLLECTION_ID>',
        )
        self.assertEqual(response.to_dict(), data)

    @respx.mock
    async def test_create_index(self):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "key": "index1",
            "description": "Speeds up lookups by email.",
            "type": "primary",
            "status": "available",
            "error": "string",
            "attributes": [],
            "lengths": [],
        }
        headers = {'Content-Type': 'application/json'}
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.databases.create_index(
            '<DATABASE_ID>',
            '<COLLECTION_ID>',
            '<KEY>',
            'key',
            [],
        )
        self.assertEqual(response.to_dict(), data)

    @respx.mock
    async def test_get_index(self):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "key": "index1",
            "description": "Speeds up lookups by email.",
            "type": "primary",
            "status": "available",
            "error": "string",
            "attributes": [],
            "lengths": [],
        }
        headers = {'Content-Type': 'application/json'}
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.databases.get_index(
            '<DATABASE_ID>',
            '<COLLECTION_ID>',
            '<KEY>',
        )
        self.assertEqual(response.to_dict(), data)

    @respx.mock
    async def test_delete_index(self):
        data = ''
        headers = {'Content-Type': 'application/json'}
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.databases.delete_index(
            '<DATABASE_ID>',
            '<COLLECTION_ID>',
            '<KEY>',
        )
        self.assertEqual(response, data)
