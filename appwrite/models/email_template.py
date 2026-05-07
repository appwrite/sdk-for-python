from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class EmailTemplate(AppwriteModel):
    """
    EmailTemplate

    Attributes
    ----------
    templateid : str
        Template type
    locale : str
        Template locale
    message : str
        Template message
    sendername : str
        Name of the sender
    senderemail : str
        Email of the sender
    replytoemail : str
        Reply to email address
    replytoname : str
        Reply to name
    subject : str
        Email subject
    """
    templateid: str = Field(..., alias='templateId')
    locale: str = Field(..., alias='locale')
    message: str = Field(..., alias='message')
    sendername: str = Field(..., alias='senderName')
    senderemail: str = Field(..., alias='senderEmail')
    replytoemail: str = Field(..., alias='replyToEmail')
    replytoname: str = Field(..., alias='replyToName')
    subject: str = Field(..., alias='subject')
