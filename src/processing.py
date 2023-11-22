from typing import Any
import re
from src.read_the_table import read_xlsx_csv_file
from data.config import PATH_CSV_FILE

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


def sorted_operation(operation_list: list[dict[Any, Any]], revers: bool = False) -> list[dict[Any, Any]] | None:
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

def operation_search(data_bank: Any, search_word: str) -> list:
    """
    Поисковой движок банковских операций
    :param data_bank: банковские операции
    :param search_word: искомое слово
    :return: новый список
    """
    def is_search(word: str, any_object: Any):
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
    pass
if __name__ == '__main__':
    print(operation_search(read_xlsx_csv_file(PATH_CSV_FILE), '2023-01-04T13:13:34Z'))