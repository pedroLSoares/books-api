from repository.books_respository import get_all, save_all
import statistics
from services.scrapping_service import Scrapper
from dto.StatsResponse import StatsResponse

def get_book_categories():
    """
        Busca todas as categorias disponíveis
    """
    all_books = get_all()
    categories = set([book.category for book in all_books])
    return list(categories)

def search_books(query: dict):
    """
        Busca todos os livros dado os parâmetros recebidos na query.
    """
    all_books = get_all()
    results = []
    for book in all_books:
        if all(str(book.model_dump()[key]) == str(value) for key, value in query.items()):
            results.append(book)
    return results

def get_books_overview():
    """
        Retorna a quantidade de livros em cada rating
    """
    all_books = get_all()
    median_price = statistics.median([book.price for book in all_books])
    rating_distribution = {
        "1.0": 0,
        "2.0": 0,
        "3.0": 0,
        "4.0": 0,
        "5.0": 0
    }
    for book in all_books:
        rating_distribution[str(book.rating)] = rating_distribution.get(str(book.rating), 0) + 1
    
    return StatsResponse(
        total_books=len(all_books),
        median_price=round(median_price, 2),
        rating_distribution=rating_distribution
    )

def get_books_by_category():
    """
        Busca a quantidade de livros por categoria
    """
    all_books = get_all()
    qty_by_category = {}
    for book in all_books:
        qty_by_category[book.category] = qty_by_category.get(book.category, 0) + 1
    
    return qty_by_category

def get_top_rated_books(limit: int):
    """"
        Busca os livros mais bem avaliados, com o limite recebido por parâmetro
    """
    all_books = get_all()
    top_rated_books = sorted(all_books, key=lambda x: x.rating, reverse=True)[:limit]
    return top_rated_books

def get_books_by_price(min: float = 0, max: float = None):
    """
        Busca os livros pelo range de preço
    """
    all_books = get_all()
    books_by_price = [book for book in all_books if book.price >= min and (max is None or book.price <= max)]
    return books_by_price


async def ingest_books_data():
    """
        Realiza a raspagem de dados de livros e os salva em um arquivo CSV
    """
    scrapper = Scrapper()
    data = await scrapper.extract_data()
    save_all(data)