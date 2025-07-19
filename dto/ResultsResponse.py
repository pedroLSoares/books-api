from typing import Generic, TypeVar
from pydantic import BaseModel

T = TypeVar('T')

class ResultsResponse(BaseModel, Generic[T]):
    results: list[T]