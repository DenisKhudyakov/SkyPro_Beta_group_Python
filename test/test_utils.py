import json
import os
from typing import Any
from unittest.mock import patch

import pytest
import requests

from data.config import FILE_PATH
from src.generators import filter_by_currency
from src.utils import get_api, transit_calculation


@pytest.fixture
def fixture():
    with open(str(FILE_PATH), "r") as file:
        bank_data = json.load(file)
        for operation in filter_by_currency(bank_obj=bank_data, currency="RUB"):
            return operation


@pytest.fixture
def fixture_with_usd():
    with open(str(FILE_PATH), "r") as file:
        bank_data = json.load(file)
        for operation in filter_by_currency(bank_obj=bank_data, currency="USD"):
            return operation


def test_transit_calculation(fixture, fixture_with_usd) -> None:
    """
    Тестирование функции transit_calculatio, в двух случаях, первый случай, когда она должна вывести сумму транзакции,
    второй случай исключение
    :param fixture: словарь с рублёвой транзакцией
    :param fixture_with_usd: словарь с валютной транзакцией
    :return: тестовая функция ничего не возвращает
    """
    assert transit_calculation(fixture) == 31957.58
    assert transit_calculation(fixture_with_usd) == 750257.56


@patch("requests.get")
def test_get(mock_get: Any) -> None:
    """
    Тестирование функции взаимодействия с АПИ
    :param mock_get: пропатченная переменная
    :return: тестовая функция ничего не возврщает
    """
    mock_get.return_value.ok = True
    with open("currency.json") as f:
        data = json.load(f)
    mock_get.return_value.json.return_value = data
    result = get_api()[0]
    response = get_api()[1]
    assert data == result
    assert mock_get.return_value.ok == response.ok
