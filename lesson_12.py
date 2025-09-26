"""
Демонстрация работы со скрытыми API сайтов:
- Nasdaq
- LME
- 5ka.ru
- Fedresurs
- kad.arbitr.ru

⚠️ Внимание:
Некоторые API могут требовать авторизацию, куки или спец. токены.
Примеры ниже даны только для демонстрации и могут не всегда работать
"как есть".
"""

import requests


def nasdaq_quote(symbol: str = "AAPL"):
    """
    Пример обращения к API Nasdaq.
    Получение информации по акции.
    """
    url = f"https://api.nasdaq.com/api/quote/{symbol}/info"
    headers = {"User-Agent": "Mozilla/5.0"}  # Nasdaq требует заголовок
    resp = requests.get(url, headers=headers)
    return resp.json()


def nasdaq_chart(symbol: str = "AAPL"):
    """
    Пример API Nasdaq для получения данных графика.
    """
    url = f"https://api.nasdaq.com/api/quote/{symbol}/chart"
    headers = {"User-Agent": "Mozilla/5.0"}
    resp = requests.get(url, headers=headers)
    return resp.json()


def lme_prices():
    """
    Пример LME (London Metal Exchange).
    Возвращает котировки металлов.
    """
    url = "https://www.lme.com/api/trading/prices"  # пример эндпоинта
    headers = {"User-Agent": "Mozilla/5.0"}
    resp = requests.get(url, headers=headers)
    return resp.json()


def fivka_products():
    """
    Пример API магазина "Пятёрочка" (5ka.ru).
    Возвращает список акционных товаров.
    """
    url = "https://5ka.ru/api/v1/special_offers/"
    resp = requests.get(url)
    return resp.json()


def fedresurs_publications():
    """
    Пример API fedresurs.ru.
    Возвращает список публикаций.
    ⚠️ Может требовать авторизацию/куки.
    """
    url = "https://fedresurs.ru/backend/portal/api/publications"
    resp = requests.get(url)
    return resp.json()


def kad_search():
    """
    Пример API kad.arbitr.ru.
    Поиск дел.
    ⚠️ Требует POST-запрос с параметрами.
    """
    url = "https://kad.arbitr.ru/Kad/SearchInstances"
    payload = {
        "Page": 1,
        "Count": 5,
        "Courts": None,
        "Judges": None,
        "CaseNumbers": None,
        "DateFrom": None,
        "DateTo": None,
        "Sides": None,
        "WithVKSInstances": False,
        "CaseCategory": None,
        "WithCourtCases": False
    }
    headers = {"User-Agent": "Mozilla/5.0", "Content-Type": "application/json"}
    resp = requests.post(url, json=payload, headers=headers)
    return resp.json()


if __name__ == "__main__":
    print("Nasdaq quote (AAPL):")
    print(nasdaq_quote())

    print("\n5ka special offers:")
    print(fivka_products())

    # ⚠️ Остальные API могут требовать авторизацию и работать нестабильно
    # print(lme_prices())
    # print(fedresurs_publications())
    # print(kad_search())
