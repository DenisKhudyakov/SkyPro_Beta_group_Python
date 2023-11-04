import pytest

from src.widget import bank_data_conversion, date_time_formatter


@pytest.mark.parametrize(
    "bank_data, result",
    [
        ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
        ("Счет 64686473678894779589", "Счет **9589"),
        ("MasterCard 7158300734726758", "MasterCard 7158 30** **** 6758"),
        ("Счет 35383033474447895560", "Счет **5560"),
        ("Visa Classic 6831982476737658", "Visa Classic 6831 98** **** 7658"),
        ("", ""),
    ],
)
def test_bank_data_conversion(bank_data: str, result: str) -> None:
    """
    Тестовая функция проверяющая правильность форматирования номера карты и номера счета.
    :param bank_data: номер счета/номер карты
    :param result: ожидаемый отформатированный результат.
    :return: тестовые функции ничего не возвращщают
    """
    assert bank_data_conversion(bank_data) == result


def test_date_time_formatter() -> None:
    """
    Тестовая функция, проверяющая форматирование даты и времени к определённому паттерну.
    :return: Тестовые фунцкии ничего не возвращают
    """
    assert date_time_formatter("2018-07-11T02:26:18.671407") == "11.07.2018"
    assert date_time_formatter("") == "Что-то пошло не так..."
