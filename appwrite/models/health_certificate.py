from typing import Any, Dict, List, Optional, Union

from pydantic import Field

from .base_model import AppwriteModel

class HealthCertificate(AppwriteModel):
    """
    Health Certificate

    Attributes
    ----------
    name : str
        Certificate name
    subjectsn : str
        Subject SN
    issuerorganisation : str
        Issuer organisation
    validfrom : str
        Valid from
    validto : str
        Valid to
    signaturetypesn : str
        Signature type SN
    """
    name: str = Field(..., alias='name')
    subjectsn: str = Field(..., alias='subjectSN')
    issuerorganisation: str = Field(..., alias='issuerOrganisation')
    validfrom: str = Field(..., alias='validFrom')
    validto: str = Field(..., alias='validTo')
    signaturetypesn: str = Field(..., alias='signatureTypeSN')
