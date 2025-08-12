from services.write_service import read_from_csv, write_to_csv
from models.Book import Book
import os
from services.scrapping_service import Scrapper

def get_all():
    if os.path.exists(os.path.join('/tmp', 'books.csv')) == False:
        """
         Caso o arquivo não exista, realiza o scraping e salva os dados no arquivo
        """
        save_all(Scrapper().extract_data())
    
    data = read_from_csv(os.path.join('/tmp', 'books.csv'))
    return list(map(lambda book: Book(**book), data))

def get_by_id(id: int):
    if os.path.exists(os.path.join('/tmp', 'books.csv')) == False:
        return []
    data = read_from_csv(os.path.join('/tmp', 'books.csv'))
    return Book(**data[id])

def save_all(data):
    write_to_csv(data, os.path.join('/tmp', 'books.csv'))
