import json
import os
from typing import Any

import pytest

from data.config import FILE_PATH_TRANSACTIONS
from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


@pytest.fixture
def bank_data() -> Any:
    with open(FILE_PATH_TRANSACTIONS, "r") as file:
        transactions = json.load(file)
        return transactions


def test_filter_by_currency(bank_data: Any) -> None:
    """
    Тестирование функции filter_by_currency
    :param bank_data: фикстура банковских данных, список со словарями
    :return: тестовая функция ничего не возвращает
    """
    usd_transactions = filter_by_currency(bank_obj=bank_data, currency="RUB")
    assert next(usd_transactions)["id"] == 873106923
    assert next(usd_transactions)["id"] == 594226727


def test_transaction_descriptions(bank_data: Any) -> None:
    """
    Тестирование функции transaction_descriptions
    :param bank_data: фикстура банковских данных, список со словарями
    :return: тестовая функция ничего не возвращает
    """
    descriptions = transaction_descriptions(bank_data)
    assert next(descriptions) == "Перевод организации"
    assert next(descriptions) == "Перевод со счета на счет"
    assert next(descriptions) == "Перевод со счета на счет"
    assert next(descriptions) == "Перевод с карты на карту"


@pytest.mark.parametrize(
    "start, end, result",
    [
        (1, 5, ["0000000000000001", "0000000000000002", "0000000000000003", "0000000000000004"]),
    ],
)
def test_card_number_generator(start: int, end: int, result: list) -> None:
    """
    тестирование функции генерации номеров карт
    :param start: параметр стартового значения карт
    :param end: параметр конечного значения карт
    :param result: список ожидаемых значений карт, если функция работает исправно
    :return: тестовая функция ничего не возвращает
    """
    for _ in range(end):
        assert next(card_number_generator(start, end)) == next(iter(result))
