from typing import Any, Generator


def filter_by_currency(bank_obj: Any, currency: str) -> Generator:
    """
    Функиция итератор, фильтрующая банковские операции по заданной валюте
    :param bank_obj: Any
    :param currency: str
    :return: generator
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
    :param trans_list:
    :return: generator
    """
    for operation in trans_list:
        yield operation["description"]


def card_number_generator(start: int, end: int) -> Generator:
    """
    Генератор номеров карт
    :param start: inr
    :param end: inr
    :return: generator
    """
    number_card_ver2 = ((16 * "0")[0 : -len(str(number))] + str(number) for number in range(start, end + 1))
    # number = "0000000000000000"
    # for i in range(start, end + 1):
    #     number_card = number[0 : -len(str(i))] + str(i)
    #     yield " ".join([number_card[0:4], number_card[4:8], number_card[8:12], number_card[12:16]])
    for one_number in number_card_ver2:
        yield one_number
