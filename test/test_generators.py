import pytest
from typing import Any
from src.generators import filter_by_currency, transaction_descriptions, card_number_generator
import json
import os

@pytest.fixture
def bank_data() -> list:
    with open(os.path.join('src', 'transactions.json'), 'r') as file:
        transactions = json.load(file)
        return transactions

def test_filter_by_currency(bank_data: Any) -> None:
    """
    Тестирование функции filter_by_currency
    :param bank_data: лсит либо, словарь
    :return: None
    """
    usd_transactions = filter_by_currency(bank_obj=bank_data, currency='RUB')
    assert next(usd_transactions)["id"] == 873106923
    assert next(usd_transactions)["id"] == 594226727


def test_transaction_descriptions(bank_data):
    descriptions = transaction_descriptions(bank_data)
    assert next(descriptions) == 'Перевод организации'
    assert next(descriptions) == 'Перевод со счета на счет'
    assert next(descriptions) == 'Перевод со счета на счет'
    assert next(descriptions) == 'Перевод с карты на карту'

@pytest.mark.parametrize('start, end, result', [(1, 5, ['0000000000000001', '0000000000000002', '0000000000000003', '0000000000000004']),
                                                ])
def test_card_number_generator(start: int, end: int, result: list) -> None:
    """
    тестирование функции генерации номеров карт
    :param start: int
    :param end: int
    :param result: list
    :return: None
    """
    assert next(card_number_generator(start, end)) == next(iter(result))

