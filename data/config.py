from pathlib import Path

ROOT_PATH = Path(__file__).parent
FILE_PATH = ROOT_PATH.joinpath("operations.json")
FILE_PATH_TRANSACTIONS = ROOT_PATH.joinpath("transactions.json")
FILE_PATH_CURRENCY = ROOT_PATH.joinpath("currency.json")
PATH_XLSX_FILE = ROOT_PATH.joinpath("transactions_excel.xlsx")
PATH_CSV_FILE = ROOT_PATH.joinpath("transactions.csv")
