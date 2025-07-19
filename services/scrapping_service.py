import requests
from bs4 import BeautifulSoup
import re
import asyncio
import httpx
import requests

class Scrapper:
    def __init__(self):
        self.baseUrl = "https://books.toscrape.com/"
        self.client = httpx.AsyncClient()

    def convert_rating_to_number(self, rating: str):
        """
        Realiza a conversão do rating para um número
        """
        mapping = {
            "one": 1,
            "two": 2,
            "three": 3,
            "four": 4,
            "five": 5
        }
        return mapping[rating.lower()]

    async def scrape_website(self, url):
        """
        Faz uma requisição para uma dada url e retorna o conteúdo formatado
        """
        try:
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
            }
            
            response = await self.client.get(url, headers=headers)
            response.raise_for_status()
            
            soup = BeautifulSoup(response.content, 'html.parser')
            
            return soup
            
        except requests.exceptions.RequestException as e:
            print(f"Erro ao fazer requisição: {e}")
            return None

    def extract_books_list(self,soup: BeautifulSoup, category: str):
        """
        Extrai uma lista de livros do objeto soup
        """
        
        data = [] # title, price, rating, availability, category, image  
        for item in soup.find_all('article'):
            data.append({
                'title': item.find('h3').find('a').get('title'),
                'price': float(item.find('p', class_='price_color').get_text().replace("£", "")),
                'currency': '£',
                'rating': self.convert_rating_to_number(item.find('p', class_='star-rating').get('class')[1]), # 1 to 5 stars need to convert to number,
                'image': self.baseUrl + re.sub(r'\.{1,2}\/', '', item.find('img').get('src')),
                'category': category
            })
        
        return data

    async def extract_page(self, url: str, categoryName: str):
        data = []
        soup = await self.scrape_website(url)
        if soup:
            data.extend(self.extract_books_list(soup, categoryName))
            hasNext = soup.find('li', class_='next')
            if hasNext:
                nextPage = hasNext.find('a').get('href')
                replacedUrl = re.sub(r'\/(\w|\-?)+\.html$', '', url)
                newUrl = replacedUrl + "/" + nextPage
                print(f"Extraindo próxima página`: {nextPage} e nova url {newUrl}")
                data.extend(await self.extract_page(replacedUrl + "/" + nextPage, categoryName))

        return data

    async def extract_data(self):
        """
            Extrai dados da baseUrl, o resultado é uma lista de livros com título, preço, avaliação, disponibilidade, categoria, imagem
        """
        data = [] # title, price, rating, availability, category, image
        tasks = []
        soup = await self.scrape_website(self.baseUrl)
        if soup:
            print("✅ Requisição realizada com sucesso!")
            print(f"Page title: {soup.title.get_text() if soup.title else 'Not found'}")

            for category in soup.find('div', class_='side_categories').find('ul').find('ul').find_all('a'):
                categoryName = category.getText().strip()
                link = category.get('href')
                tasks.append(self.extract_page(self.baseUrl + link, categoryName))

        else:
            print("❌ Erro ao extrair dados da página")

        results = await asyncio.gather(*tasks)
        for result in results:
            data.extend(result)

        await self.client.aclose()
        return data