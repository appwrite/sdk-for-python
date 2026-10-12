from typing import Any, Dict, List, Optional, Union
from ..exception import AppwriteException


def validate_row_data(
    data: Dict[str, Any],
    schema: Union[List[Any], Any]
) -> None:
    """
    Validates row data against table schema columns client-side before sending network requests.

    Parameters
    ----------
    data : Dict[str, Any]
        The row payload being inserted or updated.
    schema : Union[List[Any], ColumnList]
        A list of Column models or ColumnList representing table schema definitions.

    Raises
    ------
    AppwriteException
        If a required field is missing or an invalid data type is detected.
    """
    if not isinstance(data, dict):
        raise AppwriteException('Row data must be a dictionary/object.')

    if schema is None:
        return

    columns = getattr(schema, 'columns', schema)
    if not isinstance(columns, (list, tuple)):
        return

    type_mapping = {
        'string': (str,),
        'text': (str,),
        'varchar': (str,),
        'mediumtext': (str,),
        'longtext': (str,),
        'email': (str,),
        'url': (str,),
        'ip': (str,),
        'datetime': (str,),
        'integer': (int,),
        'bigint': (int,),
        'float': (float, int),
        'boolean': (bool,),
    }

    for col in columns:
        key = getattr(col, 'key', None) or (col.get('key') if isinstance(col, dict) else None)
        if not key:
            continue

        required = getattr(col, 'required', False) or (col.get('required', False) if isinstance(col, dict) else False)
        col_type = getattr(col, 'type', None) or (col.get('type') if isinstance(col, dict) else None)
        is_array = getattr(col, 'array', False) or (col.get('array', False) if isinstance(col, dict) else False)

        if key not in data or data[key] is None:
            if required:
                raise AppwriteException(f"Missing required attribute '{key}' based on table schema.", 400, 'attribute_required')
            continue

        val = data[key]

        if is_array:
            if not isinstance(val, (list, tuple)):
                raise AppwriteException(f"Attribute '{key}' must be a list/array.", 400, 'attribute_invalid_type')
            if col_type and col_type in type_mapping:
                expected_types = type_mapping[col_type]
                for item in val:
                    # bool is a subclass of int in Python, so check bool explicitly
                    if col_type in ('integer', 'bigint', 'float') and isinstance(item, bool):
                        raise AppwriteException(f"Element in '{key}' must be of type {col_type}, got boolean.", 400, 'attribute_invalid_type')
                    if not isinstance(item, expected_types):
                        raise AppwriteException(f"Element in '{key}' must be of type {col_type}, got {type(item).__name__}.", 400, 'attribute_invalid_type')
        else:
            if col_type and col_type in type_mapping:
                expected_types = type_mapping[col_type]
                if col_type in ('integer', 'bigint', 'float') and isinstance(val, bool):
                    raise AppwriteException(f"Attribute '{key}' must be of type {col_type}, got boolean.", 400, 'attribute_invalid_type')
                if not isinstance(val, expected_types):
                    raise AppwriteException(f"Attribute '{key}' must be of type {col_type}, got {type(val).__name__}.", 400, 'attribute_invalid_type')
