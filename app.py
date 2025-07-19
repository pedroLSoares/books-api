from fastapi import FastAPI
from handler.books_handler import router as books_router
from handler.categories_handler import router as categories_router
from handler.stats_handler import router as stats_router
from handler.jobs_handler import router as jobs_router
from handler.auth_handler import router as auth_router
from config.database_config import DatabaseConfig
from services.books_service import ingest_books_data
import uvicorn
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

app.include_router(books_router)
app.include_router(categories_router)
app.include_router(stats_router)
app.include_router(jobs_router)
app.include_router(auth_router)

app.add_api_route("/api/v1/health", lambda: {"status": "ok"})

@app.on_event("startup")
async def startup_event():
    db_config = DatabaseConfig()
    db_config.init_db()
    # await ingest_books_data()

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
    
    