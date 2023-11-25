import re
from collections import Counter
from typing import Any

from data.config import PATH_CSV_FILE
from src.read_the_table import read_xlsx_csv_file


def filter_operations(operation_list: list[dict[Any, Any]], state_value: str = "EXECUTED") -> list[Any] | None:
    """
        функцию, которая принимает на вход список словарей и значение для ключа state
        (опциональный параметр со значением по умолчанию
    EXECUTED
    ) и возвращает новый список, содержащий только те словари, у которых ключ
    state
     содержит переданное в функцию значение
        :param operation_list: список банковских операций/
        :param state_value: параметр, по котоому нужно делать фильтацию
        :return: list: отфильтрованный список банковских операций
    """
    return list(filter(lambda x: x["state"] == state_value, operation_list)) if operation_list else None


def sorted_operation(operation_list: list[Any] | None, revers: bool = False) -> list[dict[Any, Any]] | None:
    """
        функцию, которая принимает на вход список словарей и возвращает новый список,
        в котором исходные словари отсортированы по убыванию даты (ключ
    date
    ). Функция принимает два аргумента, второй необязательный задает порядок
    сортировки (убывание, возрастание)
        :param operation_list: список банковских операций
        :param revers: дополнительнй параметр для списка возрастание или убывание
        :return: возвращаем список отсортированный по дате
    """
    return sorted(operation_list, key=lambda date: date["date"], reverse=revers) if operation_list else None


def operation_search(data_bank: Any, search_word: str) -> list[Any]:
    """
    Поисковой движок банковских операций
    :param data_bank: банковские операции
    :param search_word: искомое слово
    :return: новый список
    """

    def is_search(word: str, any_object: Any) -> bool:
        """
        Булевая функция на проверку вхождения слова в объект
        :param word: искомое слово
        :param any_object: любой объект
        :return: булевая переменная
        """
        match = re.search(word, str(any_object))
        return True if match else False

    return list(filter(lambda x: is_search(search_word, x.values()), list(data_bank)))


def operation_counter(data_bank: list, operation: dict) -> dict:
    """
    Функция фильтрации категорий банковский операций и их подсчета
    :param data_bank: все банковские операции
    :param operation: словарь искомых операций с нулевыми значениями
    :return: словарь с посчитанными значениями из базы данных
    """
    category_operation = [i["description"] for i in data_bank]
    filter_category = {key: value for key, value in dict(Counter(category_operation)).items() if key in operation}
    return filter_category


if __name__ == "__main__":
    print(operation_search(read_xlsx_csv_file(PATH_CSV_FILE), "2023-01-04T13:13:34Z"))
    print(operation_counter(read_xlsx_csv_file(PATH_CSV_FILE), {"Открытие вклада": 0, "Перевод организации": 0}))
