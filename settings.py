
class Settings:
    
    en_url: str = "https://bank.gov.ua/en/markets/exchangerates"
    ua_url: str = "https://bank.gov.ua/ua/markets/exchangerates"
    
    headers: dict[str: str] = {
                "Sec-Ch-Ua": '"Not.A/Brand";v="8", "Chromium";v="114", "Opera GX";v="100"',
                "Sec-Ch-Ua-Mobile": "?0",
                "Sec-Ch-Ua-Platform": "macOS",
                "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 OPR/100.0.0.0"
    }
    
    currencies: list[str] = [
        "AUD","AZN","BYN","BGN","KRW",
        "HKD","DKK","USD","EUR","EGP",
        "JPY","PLN","INR","CAD","MXN",
        "MDL","ILS","NZD","NOK","ZAR",
        "RUB","RON","IDR","SGD","XDR",
        "KZT","TRY","HUF","GBP","CZK",
        "SEK","CHF","CNY"
    ]
    
    languages: list[str] = ['en', 'ua']