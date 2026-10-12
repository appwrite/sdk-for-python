from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr, model_validator

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

    @model_validator(mode='before')
    @classmethod
    def _apply_defaults(cls, data: Any) -> Any:
        if not isinstance(data, dict):
            return data

        data = dict(data)
        if 'templateId' not in data and 'templateid' not in data:
            data['templateId'] = ''
        if 'locale' not in data:
            data['locale'] = ''
        if 'message' not in data:
            data['message'] = ''
        if 'senderName' not in data and 'sendername' not in data:
            data['senderName'] = ''
        if 'senderEmail' not in data and 'senderemail' not in data:
            data['senderEmail'] = ''
        if 'replyToEmail' not in data and 'replytoemail' not in data:
            data['replyToEmail'] = ''
        if 'replyToName' not in data and 'replytoname' not in data:
            data['replyToName'] = ''
        if 'subject' not in data:
            data['subject'] = ''
        return data
