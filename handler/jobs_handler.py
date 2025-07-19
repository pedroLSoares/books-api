from fastapi import APIRouter
from services.books_service import ingest_books_data


router = APIRouter(
    prefix="/api/v1/jobs",
    tags=["jobs"]
)

@router.post('/scrape')
async def scrape_books_handler():
    """
        Scrape books from the website and save them to a csv file
    """
    await ingest_books_data()
    return {"status": "ok"}
