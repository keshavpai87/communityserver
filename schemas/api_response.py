from typing import Generic
from typing import TypeVar

from pydantic import BaseModel

T = TypeVar("T")


class ApiResponse(BaseModel, Generic[T]):

    responseCode: int

    responseMessage: str

    responseBody: T

    # NOTE :
    # This is the wrapper every API returns.