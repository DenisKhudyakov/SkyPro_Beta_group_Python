from src.generators import filter_by_currency
import os
import json

def transit_calculation(operation: dict) -> float | ValueError:
    """
    Функция, которая принимает на вход одну транзакцию, и возвращает сумму перевода, при условии,
    если транзакция в рублях
    :param operation: словарь с транзакцией
    :return: сумма перевода или исключение
    """
    try:
        if operation["operationAmount"]["currency"]["code"] == "RUB":
            return float(operation["operationAmount"]["amount"])
        else:
            raise ValueError("Транзакция выполнена не в рублях. Укажите транзакцию в рублях")
    except ValueError as ex:
        return ex


if __name__ == '__main__':

    with open(os.path.join('..', 'data', 'operations.json'), 'r') as file:
        bank_data = json.load(file)
        print(len(bank_data))
        for operation in filter_by_currency(bank_obj=bank_data, currency='USD'):
            print(transit_calculation(operation))