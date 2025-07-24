from services.write_service import read_from_csv
from models.Book import Book
import pathlib

def get_all():
    data = read_from_csv(pathlib.Path(__file__).resolve() / "tmp" / "books.csv").data
    return list(map(lambda book: Book(**book), data))

def get_by_id(id: int):
    data = read_from_csv(pathlib.Path(__file__).resolve() / "tmp" / "books.csv")
    return Book(**data[id])