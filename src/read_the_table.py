from typing import Any

import pandas as pd

from data.config import PATH_CSV_FILE, PATH_XLSX_FILE

one_transactions = {
    "id": None,
    "state": None,
    "date": None,
    "operationAmount": {"amount": None, "currency": {"name": None, "code": None}},
    "description": None,
    "from": None,
    "to": None,
}


def transformation_of_the_structure(list_: list, struct: dict) -> list:
    """
    Функция преобразования входного списка в словарь заданной структуры
    :param list_: список с банковскими данными
    :param struct: необходимая структура словаря
    :return: возвращемое значение список со словарём
    """
    transactions_list = []
    struct["id"] = str(list_[0])[:-2]
    struct["state"] = list_[1]
    struct["date"] = list_[2]
    struct["operationAmount"]["amount"] = list_[3]
    struct["operationAmount"]["currency"]["name"] = list_[4]
    struct["operationAmount"]["currency"]["code"] = list_[5]
    struct["description"] = list_[8]
    struct["from"] = list_[6]
    struct["to"] = list_[7]
    transactions_list.append(struct)
    return transactions_list


def read_xlsx_csv_file(file: Any) -> Any:
    """
    Функция генератор, которая читайет Эксель или CSV файл, и преобразует его в заданную пайтон структуру
    :param file: Путль до файла
    :return: Генератор списка
    """
    if str(file).endswith(".csv"):
        df = pd.read_csv(file, delimiter=";")
        for row in df.iterrows():
            yield transformation_of_the_structure(row[1].tolist(), one_transactions)
    df = pd.read_excel(file)
    for row in df.iterrows():
        yield transformation_of_the_structure(row[1].tolist(), one_transactions)


print(next(read_xlsx_csv_file(PATH_XLSX_FILE)))
print(next(read_xlsx_csv_file(PATH_CSV_FILE)))
