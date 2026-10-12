import unittest
from appwrite.exception import AppwriteException
from appwrite.utils.validator import validate_row_data


class TestRowValidation(unittest.TestCase):
    def setUp(self):
        self.mock_schema = [
            {'key': 'title', 'type': 'string', 'required': True, 'array': False},
            {'key': 'views', 'type': 'integer', 'required': False, 'array': False},
            {'key': 'rating', 'type': 'float', 'required': False, 'array': False},
            {'key': 'is_published', 'type': 'boolean', 'required': False, 'array': False},
            {'key': 'tags', 'type': 'string', 'required': False, 'array': True},
        ]

    def test_valid_payload_passes(self):
        payload = {
            'title': 'Getting Started with Appwrite',
            'views': 120,
            'rating': 4.8,
            'is_published': True,
            'tags': ['cloud', 'backend', 'python'],
        }
        # Should execute cleanly without raising
        validate_row_data(payload, self.mock_schema)

    def test_missing_required_attribute_raises(self):
        payload = {
            'views': 10,
        }
        with self.assertRaises(AppwriteException) as ctx:
            validate_row_data(payload, self.mock_schema)
        self.assertIn("Missing required attribute 'title'", str(ctx.exception))
        self.assertEqual(ctx.exception.type, 'attribute_required')

    def test_invalid_type_raises(self):
        payload = {
            'title': 12345,  # Expected string
        }
        with self.assertRaises(AppwriteException) as ctx:
            validate_row_data(payload, self.mock_schema)
        self.assertIn("Attribute 'title' must be of type string", str(ctx.exception))
        self.assertEqual(ctx.exception.type, 'attribute_invalid_type')

    def test_boolean_in_numeric_field_raises(self):
        payload = {
            'title': 'Valid Title',
            'views': True,  # In python bool is subclass of int, but schema must reject
        }
        with self.assertRaises(AppwriteException) as ctx:
            validate_row_data(payload, self.mock_schema)
        self.assertIn("Attribute 'views' must be of type integer, got boolean", str(ctx.exception))

    def test_array_attribute_validation(self):
        payload = {
            'title': 'Valid Title',
            'tags': 'not-an-array',
        }
        with self.assertRaises(AppwriteException) as ctx:
            validate_row_data(payload, self.mock_schema)
        self.assertIn("must be a list/array", str(ctx.exception))

    def test_none_schema_is_noop(self):
        # Should gracefully pass when schema is None
        validate_row_data({'title': 'Hello'}, None)


if __name__ == '__main__':
    unittest.main()
