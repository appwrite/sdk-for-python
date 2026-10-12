from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr, model_validator

from .base_model import AppwriteModel


class DedicatedDatabaseBranch(AppwriteModel):
    """
    Branch

    Attributes
    ----------
    branchid : str
        Branch identifier.
    branchname : str
        Branch name.
    namespace : str
        Kubernetes namespace where the branch is deployed.
    expiresat : float
        Unix timestamp when the branch expires.
    host : str
        Branch hostname for direct connections.
    port : Optional[float]
        Branch port. Null until the backing reports one.
    database : str
        Advertised catalog the client connects to. MySQL/MariaDB use default; Postgres uses the routing label.
    username : str
        Database username. Shared with the parent database.
    password : str
        Database password. Shared with the parent database.
    ssl : bool
        Whether SSL is required.
    engine : str
        Database engine. Possible values: postgresql, mysql, mongodb.
    connectionstring : str
        Full connection string for the branch.
    """

    branchid: str = Field(..., alias='branchId')
    branchname: str = Field(..., alias='branchName')
    namespace: str = Field(..., alias='namespace')
    expiresat: float = Field(..., alias='expiresAt')
    host: str = Field(..., alias='host')
    port: Optional[float] = Field(default=None, alias='port')
    database: str = Field(..., alias='database')
    username: str = Field(..., alias='username')
    password: str = Field(..., alias='password')
    ssl: bool = Field(..., alias='ssl')
    engine: str = Field(..., alias='engine')
    connectionstring: str = Field(..., alias='connectionString')

    @model_validator(mode='before')
    @classmethod
    def _apply_defaults(cls, data: Any) -> Any:
        if not isinstance(data, dict):
            return data

        data = dict(data)
        if 'branchId' not in data and 'branchid' not in data:
            data['branchId'] = ''
        if 'branchName' not in data and 'branchname' not in data:
            data['branchName'] = ''
        if 'namespace' not in data:
            data['namespace'] = ''
        if 'expiresAt' not in data and 'expiresat' not in data:
            data['expiresAt'] = 0
        if 'host' not in data:
            data['host'] = ''
        if 'database' not in data:
            data['database'] = ''
        if 'username' not in data:
            data['username'] = ''
        if 'password' not in data:
            data['password'] = ''
        if 'ssl' not in data:
            data['ssl'] = False
        if 'engine' not in data:
            data['engine'] = ''
        if 'connectionString' not in data and 'connectionstring' not in data:
            data['connectionString'] = ''
        return data
