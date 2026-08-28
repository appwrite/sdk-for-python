from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from .database_migration import DatabaseMigration


class DatabaseMigrationList(AppwriteModel):
    """
    Database Migrations List

    Attributes
    ----------
    total : float
        Total number of migrations that matched your query.
    migrations : List[DatabaseMigration]
        List of migrations.
    """

    total: float = Field(..., alias='total')
    migrations: List[DatabaseMigration] = Field(..., alias='migrations')
