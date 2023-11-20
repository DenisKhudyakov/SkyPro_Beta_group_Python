import pandas as pd
from data.config import PATH_CSV_FILE, PATH_XLSX_FILE
from typing import Any
from pprint import pprint


def read_xlsx_csv_file(file: Any):
    transactions_list = []
    one_transactions = {
            "id": None,
            "state": None,
            "date": None,
            "operationAmount": {
                "amount": None,
                "currency": {
                    "name": None,
                    "code": None
                }
            },
            "description": None,
            "from": None,
            "to": None
        }
    if str(file).endswith('.csv'):
        df = pd.read_csv(file, delimiter=';')
        for row in df.iterrows():
            one_transactions['id'] = str(row[1].tolist()[0])[:-2]
            one_transactions['state'] = row[1].tolist()[1]
            one_transactions['date'] = row[1].tolist()[2]
            one_transactions['operationAmount']['amount'] = row[1].tolist()[3]
            one_transactions['operationAmount']['currency']['name'] = row[1].tolist()[4]
            one_transactions['operationAmount']['currency']['code'] = row[1].tolist()[5]
            one_transactions['description'] = row[1].tolist()[8]
            one_transactions['from'] = row[1].tolist()[6]
            one_transactions['to'] = row[1].tolist()[7]
            transactions_list.append(one_transactions)
    return transactions_list

print(read_xlsx_csv_file(PATH_CSV_FILE))