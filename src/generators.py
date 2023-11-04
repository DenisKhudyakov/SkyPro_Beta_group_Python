from typing import Any, Generator


def filter_by_currency(bank_obj: Any, currency: str) -> Generator:
    """
    Функиция итератор, фильтрующая банковские операции по заданной валюте
    :param bank_obj: лист со словарями из json файла в котором банковские данные
    :param currency: название валюты, по которой будем делать фильтрацию банковских данных
    :return: возвращаем отфильтрованный генератор с данными
    """
    # Первое решение
    # return filter(lambda money_type: money_type["operationAmount"]["currency"]["code"] == currency, bank_obj)
    # Второе решение
    for money_type in bank_obj:
        if money_type["operationAmount"]["currency"]["code"] == currency:
            yield money_type


def transaction_descriptions(trans_list: list) -> Generator:
    """
    генератор, который принимает список словарей и возвращает описание каждой операции по очереди.
    :param trans_list: лист со словарями, который получаем из json файла
    :return: возвращаем генератор, который выводит назначение платежа банковских операций
    """
    for operation in trans_list:
        yield operation["description"]


def card_number_generator(start: int, end: int) -> Generator:
    """
    Генератор номеров карт
    :param start: старторвый диапазон номеров карт
    :param end: конечный диапазон номеров карт
    :return: возвращаем генратор со строковыми значениями номеров карт
    """
    number_card_ver2 = ((16 * "0")[0 : -len(str(number))] + str(number) for number in range(start, end + 1))
    # number = "0000000000000000"
    # for i in range(start, end + 1):
    #     number_card = number[0 : -len(str(i))] + str(i)
    #     yield " ".join([number_card[0:4], number_card[4:8], number_card[8:12], number_card[12:16]])
    for one_number in number_card_ver2:
        yield one_number
