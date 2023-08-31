import requests
from simple_term_menu import TerminalMenu
from art import tprint
from bs4 import BeautifulSoup
from settings import Settings


def get_page(url=Settings.ua_url) -> str:
    return requests.get(url, headers=Settings.headers).text

def bs4(response: str) -> BeautifulSoup:
    return BeautifulSoup(response, "lxml")

def get_rate(soup: BeautifulSoup, code: str) -> float:
    return soup.find("td", string=code).find_parent().find("td", attrs={"data-label": "Офіційний курс"}).text

def amount_of_currency(soup: BeautifulSoup, code: str) -> int:
    return soup.find("td", string=code).find_parent().find("td", attrs={"data-label": "Кількість одиниць валюти"}).text

def name_of_currency(lang: str, code: str) -> str:
    match lang:
        case 'en':
            soup = bs4(get_page(Settings.en_url))
            return soup.find("td", string=code).find_parent().find("td", attrs={"data-label": "Currency name"}).text
        case 'ua':
            soup = bs4(get_page(Settings.ua_url))
            return soup.find("td", string=code).find_parent().find("td", attrs={"data-label": "Назва валюти"}).text

def get_date(soup: BeautifulSoup):
    return soup.find("span", attrs={"id": "exchangeDate"}).text
    
def choose_lang() -> str:
    print("Choose lang:")
    menu = TerminalMenu(Settings.languages)
    lang = Settings.languages[menu.show()]
    return lang

def input_loop(lang: str) -> str:
    while True:
        match lang:
            case 'en':
                print(f"Do u need a list of currencies['lc'] or u want to type manual['tm']?")
                list_of_commands = ['lc', 'tm']
                menu = TerminalMenu(list_of_commands)
                input_response = list_of_commands[menu.show()]
            case 'ua':
                print(f"Тобі потрібен список валют['lc'] чи Ти напишеш вручну['tm']?")
                list_of_commands = ['lc', 'tm']
                menu = TerminalMenu(list_of_commands)
                input_response = list_of_commands[menu.show()]
        match input_response:
            case "lc":
                menu = TerminalMenu(Settings.currencies)
                code_of_currency = Settings.currencies[menu.show()]
                break
            case "tm":
                while True:
                    code_of_currency = input("Type code of currency(example: USD or usd): ").upper()
                    if code_of_currency in Settings.currencies:
                        break
                    else:
                        print("Code doesn't match any currency")
                break
    return code_of_currency

def main():
    tprint("ExchangeRateToUAH")
    soup = bs4(get_page())
    lang = choose_lang()
    match lang:
        case 'en':
            print("Hello, how do u want to choose currency?")
        case 'ua':
            print("Привіт, вибери спосіб введення валюти")
    code = input_loop(lang)
    rate = get_rate(soup, code)
    amount = amount_of_currency(soup, code)
    name = name_of_currency(lang, code)
    date = get_date(soup)
    match lang:
        case 'en':
            if code == "RUB":
                print(f"On date: {date}\n1 RUB cost 3/4 shit of dog")
                print("Russian battleship go f*ck yourself!")
            else:
                print(f"On date: {date}\nExchange {name.lower().strip()}({code}) to gryvnia(UAH): {rate} UAH to {amount} {code}")
                print("Thank's for using!")
        case 'ua':
            if code == "RUB":
                print(f"На: {date}\n1 RUB коштує 3/4 гівна собаки")
                print("російський воєнний корабель іди на*уй!")
            else:
                print(f"На: {date}\nКурс {name.lower().strip()}({code}) до гривні(UAH): {rate} UAH до {amount} {code}")
                print("Дякую за користування!")
    


if __name__ == "__main__":
    main()