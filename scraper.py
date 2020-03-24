import requests
from bs4 import BeautifulSoup

def check_cases(country):
    URL = 'https://www.worldometers.info/coronavirus/country/' + country + '/'
    headers = {"User-Agemt": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:74.0) Gecko/20100101 Firefox/74.0'}
    page = requests.get(URL, headers = headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    numbers = soup.find_all('div', class_ = "maincounter-number")
    pure_numbers = []
    for pn in numbers:
        pn.find_all('span')
        pure_numbers.append(pn.text.strip())
        
    return pure_numbers