import datetime

import pytest

from src.decorators import log, my_function, my_function1, my_function2


@pytest.fixture
def numbers_and_data() -> tuple:
    """
    Фикстура с данными для теста
    :return: кортеж с датой и временем и переменными фукнции
    """
    date_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return date_time, 2, 2


def test_my_function(numbers_and_data: tuple) -> None:
    """
    тестирование декорированной функции my_function, записывает данный в файл и сравниваем с желаемой записью
    :param numbers_and_data: кортеж из фикстуры
    :return: тестовая функция ничего не возвращает
    """
    date_time, a, b = numbers_and_data
    my_function(a, b)
    with open("mylog.txt", "r") as f:
        result = f"{date_time} {my_function.__name__} ok"
        log_text = f.read().split("\n")
        assert result in log_text


def test_my_function1(numbers_and_data: tuple) -> None:
    """
    Тестирование функции. в которой вызывается исключение
    :param numbers_and_data: кортеж из фикстуры
    :return: тестовая функция ничего не возвращает
    """
    date_time, a, b = numbers_and_data
    my_function1(a, b)
    with open("mylog.txt", "r") as f:
        result = f"{date_time} {my_function1.__name__} error: <division by zero>. Inputs: (({a}, {b}), {{}})"
        log_text = f.read().strip().split("\n")
        assert result in log_text


def test_my_function2(numbers_and_data: tuple) -> None:
    """
    Тестирование функции, которая должна возвращать None, т.к. он просто выводит сообщение в консоль
    :param numbers_and_data: кортеж из фикстуры
    :return: тестовая функция ничего не возвращает
    """
    date_time, a, b = numbers_and_data
    assert my_function2(a, b) is None
