import pytest

from src.processing import filter_operations, sorted_operation


@pytest.fixture
def bank_data() -> list:
    """
    Фиксированные банковские данные
    :return: банковские данные в виде списка словарей
    """
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]


def test_filter_operations(bank_data: list) -> None:
    """
    Тестовая функция для проверки фильтрации банковских данных
    :param bank_data: банковские данные в виде списка словарей
    :return: тестовые функции ничего не возвращают
    """
    assert filter_operations(bank_data) == [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]
    assert filter_operations([]) is None


def test_sorted_operation(bank_data: list) -> None:
    """
    тестовая функция для проверки фильтрации банковских данных
    :param bank_data: банковские данные в виде списка словарей
    :return: тестовые функции ничего не возвращают
    """
    assert sorted_operation(bank_data) == [
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    ]
    assert sorted_operation([]) is None
