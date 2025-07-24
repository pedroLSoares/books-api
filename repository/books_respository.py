from services.write_service import read_from_csv, write_to_csv
from models.Book import Book
import os


def get_all():
    data = read_from_csv(os.path.join('/tmp', 'books.csv'))
    return list(map(lambda book: Book(**book), data))

def get_by_id(id: int):
    data = read_from_csv(os.path.join('/tmp', 'books.csv'))
    return Book(**data[id])

def save_all(data):
    write_to_csv(data, os.path.join('/tmp', 'books.csv'))
