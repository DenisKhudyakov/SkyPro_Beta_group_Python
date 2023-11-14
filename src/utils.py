import json
import os
from typing import Any

from src.generators import filter_by_currency


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


def transit_calculation(operation: dict) -> float | ValueError:
    """
    Функция, которая принимает на вход одну транзакцию, и возвращает сумму перевода, при условии,
    если транзакция в рублях
    :param operation: словарь с транзакцией
    :return: сумма перевода или исключение
    """
    try:
        if operation["operationAmount"]["currency"]["code"] == "RUB":
            return float(operation["operationAmount"]["amount"])
        else:
            raise ValueError("Транзакция выполнена не в рублях. Укажите транзакцию в рублях")
    except ValueError as ex:
        return ex


if __name__ == "__main__":
    with open(os.path.join("..", "data", "operations.json"), "r") as file:
        bank_data = json.load(file)
        print(len(bank_data))
        for operation in filter_by_currency(bank_obj=bank_data, currency="USD"):
            print(transit_calculation(operation))
