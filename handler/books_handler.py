from fastapi import Request, APIRouter, HTTPException
from services.books_service import search_books, get_top_rated_books, get_books_by_price
from repository.books_respository import get_all, get_by_id
from models.Book import Book
import logging
from dto.BookSearchResponse import BookSearchResponse
from dto.ResultsResponse import ResultsResponse

logger = logging.getLogger(__name__)

router = APIRouter(
    prefix="/api/v1/books",
    tags=["books"]
)

@router.get('', response_model=list[Book])
def get_books_handler():
    """
        Get all books, if the file does not exist, it will be created by scraping the website
    """
    try:
        logger.info("Getting all books")
        data = get_all()
        return data
    except Exception as e:
        logger.error(f"Error getting books: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@router.get('/search', response_model=BookSearchResponse)
def search_books_handler(req: Request):
    """
        Search books by title, price, rating, availability, category, image
    """
    data = search_books(dict(req.query_params))

    return BookSearchResponse(results=data)

@router.get('/top-rated', response_model=ResultsResponse[Book])
def get_top_rated_books_handler(limit: int = 10):
    """
        Get top rated books, returning the top 10 by default
    """
    books = get_top_rated_books(limit)
    return ResultsResponse(results=books)


@router.get('/price-range', response_model=ResultsResponse[Book])
def get_books_price_range_handler(min: float = 0, max: float = None):
    """
        Get books by price range
    """
    books = get_books_by_price(min, max)
    return ResultsResponse(results=books)

@router.get('/{id}', response_model=Book)
def get_book_by_id_handler(id: int):
    """
        Get book by id
    """
    data = get_by_id(id)

    return data



