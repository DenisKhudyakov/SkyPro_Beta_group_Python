from datetime import datetime

from widget import date_time_formatter


def filter_operations(operation_list: list, state_value="EXECUTED") -> list:
    """
        функцию, которая принимает на вход список словарей и значение для ключа state
        (опциональный параметр со значением по умолчанию
    EXECUTED
    ) и возвращает новый список, содержащий только те словари, у которых ключ
    state
     содержит переданное в функцию значение
        :param operation_list:
        :param state_value:
        :return: list
    """
    return list(filter(lambda x: x["state"] == state_value, operation_list))


def sorted_operation(operation_list: list, revers=True) -> list:
    """
        функцию, которая принимает на вход список словарей и возвращает новый список,
        в котором исходные словари отсортированы по убыванию даты (ключ
    date
    ). Функция принимает два аргумента, второй необязательный задает порядок
    сортировки (убывание, возрастание)
        :param operation_list:
        :param revers:
        :return:
    """
    return sorted(
        operation_list,
        key=lambda date: datetime.strptime(date_time_formatter(date["date"]), "%d.%m.%Y"),
        reverse=revers,
    )
