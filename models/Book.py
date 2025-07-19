from pydantic import BaseModel

class Book(BaseModel):
    title: str
    price: float
    currency: str
    rating: float
    category: str
    image: str