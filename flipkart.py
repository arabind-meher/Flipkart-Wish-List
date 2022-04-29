import requests
from bs4 import BeautifulSoup


class Flipkart:
    def __init__(self) -> None:
        self.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:99.0) Gecko/20100101 Firefox/99.0",
                       "X-Amzn-Trace-Id": "Root=1-626a76bd-48b1b0d379fec22a4ca3a21f"}
    
    @staticmethod
    def format_price(price: str) -> float:
        price = price.replace(',', '')
        return float(price[1:])

    def get_price(self, url: str) -> tuple:
        page = BeautifulSoup(requests.get(url, headers=self.headers).content, features='html.parser')
        title = page.find(class_='B_NuCI').get_text()
        price = page.find(class_='_30jeq3 _16Jk6d').get_text()
        image = page.find(class_='q6DClP')['src']
        return title, self.format_price(price), image
