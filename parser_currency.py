import requests
from bs4 import BeautifulSoup

EURO_RUB = "https://www.google.com/search?q=rehc+tdhj&oq"
DOLLAR_RUB = "https://www.google.com/search?q=%D0%BA%D1%83%D1%80%D1%81+%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80%D0%B0"
LIRA_RUB = "https://www.google.com/search?q=%D0%BA%D1%83%D1%80%D1%81+%D0%BB%D0%B8%D1%80%D1%8B"
Headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)"" Chrome/"
                             "99.0.4844.51 Safari/537.36"}


def check_currency_lira():
    return "1 Турецкая лира = " + str(float(get_currency_price_lira().replace(",", "."))) + " рубля(ей)"


def get_currency_price_lira():
    full_page = requests.get(LIRA_RUB, headers=Headers)

    soup = BeautifulSoup(full_page.content, "html.parser")

    convert = soup.findAll("span", {"class": "DFlfde", "data-precision": "2"})

    return convert[0].text


def check_currency_euro():
    return "1 Евро = " + str(float(get_currency_price_euro().replace(",", "."))) + " рубля(ей)"


def get_currency_price_euro():
    full_page = requests.get(EURO_RUB, headers=Headers)

    soup = BeautifulSoup(full_page.content, "html.parser")

    convert = soup.findAll("span", {"class": "DFlfde", "data-precision": "2"})

    return convert[0].text


def check_currency_dollar():
    return "1 Американский доллар = " + str(float(get_currency_price_euro().replace(",", "."))) + " рубля(ей)"


def get_currency_price_dollar():
    full_page = requests.get(DOLLAR_RUB, headers=Headers)

    soup = BeautifulSoup(full_page.content, "html.parser")

    convert = soup.findAll("span", {"class": "DFlfde", "data-precision": "2"})

    return convert[0].text
