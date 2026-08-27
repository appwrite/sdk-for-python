from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

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
    port : float
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
    port: float = Field(..., alias='port')
    database: str = Field(..., alias='database')
    username: str = Field(..., alias='username')
    password: str = Field(..., alias='password')
    ssl: bool = Field(..., alias='ssl')
    engine: str = Field(..., alias='engine')
    connectionstring: str = Field(..., alias='connectionString')
