from repository.books_respository import get_all
import statistics
from services.scrapping_service import Scrapper
from services.write_service import write_to_csv
import os



def get_book_categories():
    all_books = get_all()
    categories = set([book["category"] for book in all_books])
    return list(categories)

def search_books(query: dict):
    all_books = get_all()
    results = []
    for book in all_books:
        if all(book[key] == value for key, value in query.items()):
            results.append(book)
    return results

def get_books_overview():
    all_books = get_all()
    median_price = statistics.median([book["price"] for book in all_books])
    rating_distribution = {}
    for book in all_books:
        rating_distribution[book["rating"]] = rating_distribution.get(book["rating"], 0) + 1
    
    return {
        "total_books": len(all_books),
        "median_price": median_price,
        "rating_distribution": rating_distribution
    }

def get_books_by_category():
    all_books = get_all()
    qty_by_category = {}
    for book in all_books:
        qty_by_category[book["category"]] = qty_by_category.get(book["category"], 0) + 1
    
    return qty_by_category

def get_top_rated_books(limit: int):
    all_books = get_all()
    top_rated_books = sorted(all_books, key=lambda x: x["rating"], reverse=True)[:limit]
    return top_rated_books

def get_books_by_price(min: float = 0, max: float = None):
    all_books = get_all()
    books_by_price = [book for book in all_books if book["price"] >= min and (max is None or book["price"] <= max)]
    return books_by_price


async def ingest_books_data():
    scrapper = Scrapper()
    data = await scrapper.extract_data()
    write_to_csv(data, os.path.join('/tmp', 'books.csv'))