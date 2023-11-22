from typing import Any

import pandas as pd

from data.config import PATH_CSV_FILE, PATH_XLSX_FILE




def transformation_of_the_structure(list_: list) -> list:
    """
    Функция преобразования входного списка в словарь заданной структуры
    :param list_: список с банковскими данными
    :param struct: необходимая структура словаря
    :return: возвращемое значение список со словарём
    """
    one_transactions = {
        "id": None,
        "state": None,
        "date": None,
        "operationAmount": {"amount": None, "currency": {"name": None, "code": None}},
        "description": None,
        "from": None,
        "to": None,
    }
    one_transactions["id"] = str(list_[0])[:-2]
    one_transactions["state"] = list_[1]
    one_transactions["date"] = list_[2]
    one_transactions["operationAmount"]["amount"] = list_[3]
    one_transactions["operationAmount"]["currency"]["name"] = list_[4]
    one_transactions["operationAmount"]["currency"]["code"] = list_[5]
    one_transactions["description"] = list_[8]
    one_transactions["from"] = list_[6]
    one_transactions["to"] = list_[7]
    return one_transactions


def read_xlsx_csv_file(file: Any) -> Any:
    """
    Функция генератор, которая читайет Эксель или CSV файл, и преобразует его в заданную пайтон структуру
    :param file: Путль до файла
    :return: Генератор списка
    """
    if str(file).endswith(".csv"):
        df = pd.read_csv(file, delimiter=";")
        for row in df.iterrows():
            yield transformation_of_the_structure(row[1].tolist())
    else:
        df = pd.read_excel(file)
        for row in df.iterrows():
            yield transformation_of_the_structure(row[1].tolist())

if __name__ == '__main__':
    # print(next(read_xlsx_csv_file(PATH_XLSX_FILE)))
    print(list(read_xlsx_csv_file(PATH_CSV_FILE)))

