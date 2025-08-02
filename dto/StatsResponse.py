from pydantic import BaseModel

class StatsResponse(BaseModel):
    total_books: int
    median_price: float
    rating_distribution: dict[float, int]