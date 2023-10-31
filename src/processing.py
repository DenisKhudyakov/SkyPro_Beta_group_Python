


def filter_operations(operation_list: list, state_value: str = "EXECUTED") -> list:
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


def sorted_operation(operation_list: list[dict], revers: bool = False) -> list[dict]:
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


print(sorted_operation([
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]))