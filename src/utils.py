import json
import os
import requests
import functools
from typing import Any, Callable
from src.generators import filter_by_currency
from dotenv import load_dotenv
def get_currency_exchange_rate(currency: str) -> float:
    with open('currency.json', 'r', encoding='UTF-8') as file:
        cbr_data = json.load(file)
    return cbr_data["Valute"][currency]["Value"]

def converter_change(func_with_currency_rate: Callable, currensy: str = 'USD'):
    def wrapper(func):
        @functools.wraps(func)
        def inner(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
            except ValueError:
                result = round(float(args[0]["operationAmount"]["amount"]) * func_with_currency_rate(currensy), 2)
            return result
        return inner
    return wrapper

def get_json(any_path: str) -> list[dict[Any, Any]]:
    """
    Функция получает на вход путь до файла, и выводит список со словарями
    :param any_path: путь в виде строки
    :return: словарь, если файл json без ошибок
    """
    try:
        with open(any_path, "r", encoding="UTF-8") as file:
            return json.load(file)
    except json.JSONDecodeError:
        return []
    except (TypeError, KeyError, ValueError):
        return []

@converter_change(get_currency_exchange_rate)
def transit_calculation(operation: dict) -> float | ValueError:
    """
    Функция, которая принимает на вход одну транзакцию, и возвращает сумму перевода, при условии,
    если транзакция в рублях
    :param operation: словарь с транзакцией
    :return: сумма перевода или исключение
    """

    if operation["operationAmount"]["currency"]["code"] == "RUB":
        return float(operation["operationAmount"]["amount"])
    else:
        raise ValueError("Транзакция выполнена не в рублях. Укажите транзакцию в рублях")

def get_api(url: str) -> None:
    """
    Функция отправляет запрос на сайт ЦБ РФ и получает курс валют в формате JSON
    :param url: строка с адресом
    :return: ничего не возвращаем
    """
    load_dotenv()
    url_api = os.getenv(url)
    response = requests.get(url_api)
    data_dict = response.json()
    with open('currency.json', 'w') as file:
        json.dump(data_dict, file, indent=4)

def get_currency_exchange_rate(currency: str) -> float:
    with open('currency.json', 'r', encoding='UTF-8') as file:
        cbr_data = json.load(file)
    return cbr_data["Valute"][currency]["Value"]


if __name__ == "__main__":
    with open(os.path.join("..", "data", "operations.json"), "r") as file:
        bank_data = json.load(file)
        for operation in filter_by_currency(bank_obj=bank_data, currency="USD"):
            print(transit_calculation(operation))
    # get_api('URL')


