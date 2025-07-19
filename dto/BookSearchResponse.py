from pydantic import BaseModel
from models.Book import Book

class BookSearchResponse(BaseModel):
    results: list[Book]