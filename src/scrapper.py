import requests
import pandas
from datetime import datetime
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen

class scrapper :
    def crawller(link): 
        response = requests.get(link, headers={'User-Agent': 'Chrome/117.0.0.0'})
        response.raise_for_status()
        result = BeautifulSoup(response.text, 'html.parser')
        article = result.find_all('article')
        link = article[0].find('a')['href']
        return link
