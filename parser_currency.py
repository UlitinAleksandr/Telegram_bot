import requests
from bs4 import BeautifulSoup

LIRA_RUB = "https://www.google.com/search?q=%D0%BA%D1%83%D1%80%D1%81+%D0%BB%D0%B8%D1%80%D1%8B"
Headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)"" Chrome/"
                      "99.0.4844.51 Safari/537.36"}


def check_currency_lira():
    return float(get_currency_price_lira().replace(",", "."))


def get_currency_price_lira():
    full_page = requests.get(LIRA_RUB, headers=Headers)

    soup = BeautifulSoup(full_page.content, "html.parser")

    convert = soup.findAll("span", {"class": "DFlfde", "data-precision": "2"})

    return convert[0].text


if __name__ == '__main__':
    check_currency_lira()