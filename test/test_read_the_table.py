from typing import Any
from unittest.mock import patch

import pytest

from data.config import PATH_CSV_FILE
from src.read_the_table import read_xlsx_csv_file


@pytest.fixture()
def transaction_fixture() -> list:
    return [
        {
            "id": "650703",
            "state": "EXECUTED",
            "date": "2023-09-05T11:30:32Z",
            "operationAmount": {"amount": 16210.0, "currency": {"name": "Sol", "code": "PEN"}},
            "description": "Перевод организации",
            "from": "Счет 58803664561298323391",
            "to": "Счет 39745660563456619397",
        }
    ]


@patch("src.read_the_table.read_xlsx_csv_file")
def test_read_xlsx_csv_file(mock_get: Any, transaction_fixture: list) -> None:
    """
    Тестовая функция функцкии read_xlsx_csv_file
    :param mock_get: пропатченная функция
    :param transaction_fixture: фикстура с данными
    :return: тестовая функция ничего не позвращает
    """
    mock_get.return_value = transaction_fixture
    assert next(read_xlsx_csv_file(PATH_CSV_FILE)) == mock_get.return_value
