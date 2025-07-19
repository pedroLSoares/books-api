from services.write_service import read_from_csv
from models.Book import Book

def get_all():
    data = read_from_csv("books.csv")
    return list(map(lambda book: Book(**book), data))

def get_by_id(id: int):
    data = read_from_csv("books.csv")
    return Book(**data[id])