from pydantic import BaseModel
from typing import Any, Optional


class DefaultResponse(BaseModel):
    """ Стандартный ответ """
    error: Optional[bool]
    message: Optional[str]
    payload: Optional[Any]
