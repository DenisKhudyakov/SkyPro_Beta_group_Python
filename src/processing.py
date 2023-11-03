from typing import Any


def filter_operations(operation_list: list[Any] | None, state_value: str = "EXECUTED") -> list[Any]:
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


def sorted_operation(operation_list: list[dict[Any, Any]] | None, revers: bool = False) -> list[dict[Any, Any]]:
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
