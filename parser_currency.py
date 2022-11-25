import requests
from bs4 import BeautifulSoup

EURO_RUB = "https://goo.su/euro_pa"
DOLLAR_RUB = "https://goo.su/dollar"
LIRA_RUB = "https://goo.su/lira"
Headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)"" Chrome/"
                             "99.0.4844.51 Safari/537.36"}


def check(value):
    return str(float(get_value(value).replace(',', '.'))) + " RUB"


def get_value(value):
    full_page = requests.get(value, headers=Headers)
    soup = BeautifulSoup(full_page.content, "html.parser")
    convert = soup.findAll("span", {"class": "DFlfde", "data-precision": "2"})
    return convert[0].text

