import json
from typing import Any

def filter_by_currency(bank_obj: Any, currency: str):
    """
    Функиция итератор, фильтрующая банковские операции по заданной валюте
    :param bank_obj: Any
    :param currency: str
    :return: interator
    """
    # Первое решение
    # return filter(lambda money_type: money_type["operationAmount"]["currency"]["code"] == currency, bank_obj)
    # Второе решение
    for money_type in bank_obj:
        if money_type["operationAmount"]["currency"]["code"] == currency:
            yield money_type




with open('transactions.json', 'r') as file:
    transactions = json.load(file)
    usd_transactions = filter_by_currency(transactions, "RUB")
    for _ in range(2):
        print(next(usd_transactions)["id"])


