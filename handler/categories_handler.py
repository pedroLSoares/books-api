from fastapi import APIRouter
from services.books_service import get_book_categories
from dto.ResultsResponse import ResultsResponse

router = APIRouter(
    prefix="/api/v1/categories",
    tags=["categories"]
)

@router.get('', response_model=ResultsResponse[str])
def get_categories_handler():
    """
        Get all book available categories
    """
    categories = get_book_categories()
    return ResultsResponse(results=categories)
