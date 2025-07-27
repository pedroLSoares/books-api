from fastapi import APIRouter, HTTPException
from services.books_service import ingest_books_data
from middleware.TokenMiddleware import JWTBearer
from fastapi import Depends
import logging

logger = logging.getLogger(__name__)

router = APIRouter(
    prefix="/api/v1/jobs",
    tags=["jobs"]
)

@router.post('/scrape', dependencies=[Depends(JWTBearer())])
async def scrape_books_handler():
    """
        Scrape books from the website and save them to a csv file
    """
    try:
        await ingest_books_data()
        return {"status": "ok"}
    except Exception as e:
        logger.error(f"Error scraping books: {e}")
        raise HTTPException(status_code=500, detail=str(e))
