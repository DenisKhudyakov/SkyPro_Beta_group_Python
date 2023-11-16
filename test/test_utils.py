import json
from typing import Any
from unittest.mock import patch

import pytest

from data.config import FILE_PATH, FILE_PATH_CURRENCY
from src.generators import filter_by_currency
from src.utils import get_api, get_currency_exchange_rate, transit_calculation


@pytest.fixture
def fixture() -> Any:
    with open(str(FILE_PATH), "r") as file:
        bank_data = json.load(file)
        for operation in filter_by_currency(bank_obj=bank_data, currency="RUB"):
            return operation


@pytest.fixture
def fixture_with_usd() -> Any:
    with open(str(FILE_PATH), "r") as file:
        bank_data = json.load(file)
        for operation in filter_by_currency(bank_obj=bank_data, currency="USD"):
            return operation


def test_transit_calculation(fixture: Any, fixture_with_usd: Any) -> None:
    """
    Тестирование функции transit_calculatio, в двух случаях, первый случай, когда она должна вывести сумму транзакции,
    второй случай исключение
    :param fixture: словарь с рублёвой транзакцией
    :param fixture_with_usd: словарь с валютной транзакцией
    :return: тестовая функция ничего не возвращает
    """
    assert transit_calculation(fixture) == 31957.58
    assert transit_calculation(fixture_with_usd) == round(8221.37 * get_currency_exchange_rate("USD"), 2)


@patch("requests.get")
def test_get(mock_get: Any) -> None:
    """
    Тестирование функции взаимодействия с АПИ
    :param mock_get: пропатченная переменная
    :return: тестовая функция ничего не возврщает
    """
    mock_get.return_value.ok = True
    with open(FILE_PATH_CURRENCY) as f:
        data = json.load(f)
    mock_get.return_value.json.return_value = data
    result = get_api()[0]
    response = get_api()[1]
    assert data == result
    assert mock_get.return_value.ok == response.ok
