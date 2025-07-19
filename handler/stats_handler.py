from fastapi import APIRouter
from services.books_service import get_books_overview, get_books_by_category
from dto.ResultsResponse import ResultsResponse

router = APIRouter(
    prefix="/api/v1/stats",
    tags=["stats"]
)

@router.get('/overview', response_model=ResultsResponse[dict[str, int | float]])
def get_books_overview_handler():
    """"
        Get overview of books returning the total number of books, the median price and the rating distribution
    """
    overview = get_books_overview()
    return ResultsResponse(results=overview)

@router.get('/categories', response_model=ResultsResponse[dict[str, int]])
def get_books_categories_handler():
    """
        Get the number of books by category
    """
    categories = get_books_by_category()
    return ResultsResponse(results=categories)
