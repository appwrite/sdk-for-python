from typing import Any, Dict, List, Optional, Union

from pydantic import Field

from .base_model import AppwriteModel

class AlgoScryptModified(AppwriteModel):
    """
    AlgoScryptModified

    Attributes
    ----------
    type : str
        Algo type.
    salt : str
        Salt used to compute hash.
    saltseparator : str
        Separator used to compute hash.
    signerkey : str
        Key used to compute hash.
    """
    type: str = Field(..., alias='type')
    salt: str = Field(..., alias='salt')
    saltseparator: str = Field(..., alias='saltSeparator')
    signerkey: str = Field(..., alias='signerKey')
