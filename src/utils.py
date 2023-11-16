import functools
import json
import os
from typing import Any, Callable

import requests
from dotenv import load_dotenv

from data.config import FILE_PATH_CURRENCY
from src.generators import filter_by_currency


def get_currency_exchange_rate(currency: str) -> Any:
    """
    Функция получения курса валют
    :param currency: Интересующая валюта
    :return: курс
    """
    with open(FILE_PATH_CURRENCY, "r", encoding="UTF-8") as file:
        cbr_data = json.load(file)
    return cbr_data["Valute"][currency]["Value"]


def converter_change(func_with_currency_rate: Callable, currensy: str = "USD") -> Callable:
    """
    Декоратор конвертер валюты
    :param func_with_currency_rate: функция, которая даёт нам текущий курс
    :param currensy: Валюта, по умолчанию доллары
    :return: Возвращаем преобразованную функцию
    """

    def wrapper(func: Callable) -> Callable:
        @functools.wraps(func)
        def inner(*args: Any, **kwargs: Any) -> Any:
            try:
                result = func(*args, **kwargs)
            except ValueError:
                result = round(float(args[0]["operationAmount"]["amount"]) * func_with_currency_rate(currensy), 2)
            return result

        return inner

    return wrapper


def get_json(any_path: str) -> Any:
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


def get_api() -> tuple:
    """
    Функция отправляет запрос на сайт ЦБ РФ и получает курс валют в формате JSON
    :param url: строка с адресом
    :return: ничего не возвращаем
    """
    load_dotenv()
    url_api = os.getenv("URL")
    if url_api is not None:
        response = requests.get(url_api)
    data_dict = response.json()
    with open("currency.json", "w") as file:
        json.dump(data_dict, file, indent=4)
    return data_dict, response


if __name__ == "__main__":
    with open(os.path.join("..", "data", "operations.json"), "r") as file:
        bank_data = json.load(file)
        for operation in filter_by_currency(bank_obj=bank_data, currency="USD"):
            print(transit_calculation(operation))

    get_api()
