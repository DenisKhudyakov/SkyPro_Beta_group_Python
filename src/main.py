# маскировка номеров карт и счетов
# пути к файлам
from data.config import FILE_PATH, PATH_CSV_FILE, PATH_XLSX_FILE
# 1) функция-генератор с сортировкой списка транзакций по валюте
# 2) функция-генератор возвращающая описание каждой операции из списка транзакций
# 3) генератор номеров карт в заданном диапазоне
from src.generators import card_number_generator, filter_by_currency, transaction_descriptions
from src.masks import maskin_bil_number, masking_the_card
# функция поиска операций с определенными словами в описании
# функция подсчета количества операций определенной категории
# фильтровка списка транзакций по статусу (статус передается параметром),
# сортировка по дате списка транзакций с указанием направления сортировки (по возрастанию/по убыванию)
from src.processing import filter_operations, operation_counter, operation_search, sorted_operation
# функция чтения csv файла, функция чтения excel файла
from src.read_the_table import read_xlsx_csv_file
# функция чтения json файла
from src.utils import get_json
# маскировка строки с номером в зависимости от типа (Счет или карта)
from src.widget import bank_data_conversion, date_time_formatter


def main() -> None:
    while True:
        print(
            """
Программа: Привет! Добро пожаловать в программу работы с банковскими транзакициями. 
Выберите необходимый пункт меню:
1. Получить информацию о транзакциях из json файла
2. Получить информацию о транзакциях из csv файла
3. Получить информацию о транзакциях из xlsx файла
Для выхода нажмите "q"
"""
        )
        answer_user = input("Пользователь: ")
        match answer_user:
            case "1":
                print("Программа: Для обработки выбран json файл.")
                bank_data = get_json(FILE_PATH)
            case "2":
                print("Программа: Для обработки выбран csv файл")
                bank_data = read_xlsx_csv_file(PATH_CSV_FILE)
            case "3":
                print("Программа: Для обработки выбран xlsx файл")
                bank_data = read_xlsx_csv_file(PATH_XLSX_FILE)
            case "q":
                print("Приложение завершается")
                break
        print(
            """
Программа: Введите статус по которому необходимо выполнить фильтрацию. 
Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING
"""
        )
        answer_user = input("Пользователь: ").upper()
        filter_bank_data = (
            filter_operations(bank_data, state_value=answer_user)
            if answer_user in ["EXECUTED", "CANCELED", "PENDING"]
            else print(f'Программа: Статус операции "{answer_user}" недоступен.')
        )
        print("Программа: Отсортировать операции по дате? Да/Нет")
        answer_user = input("Пользователь: ").lower()
        if answer_user == "да":
            print("Программа: Отсортировать по возрастанию или по убыванию?")
            answer_user = input("Пользователь: по возрастанию/по убыванию ").lower()
            if answer_user == "по возрастанию":
                filter_bank_data = sorted_operation(filter_bank_data)
            elif answer_user == "по убыванию":
                filter_bank_data = sorted_operation(filter_bank_data, revers=True)
            else:
                print("Повторите попытку")
                continue
        print("Программа: Выводить только рублевые транзакции? Да/Нет")
        answer_user = input("Пользователь: да/нет ")
        if answer_user == "да":
            filter_bank_data = list(filter_by_currency(filter_bank_data, "RUB"))
        print("Программа: Отфильтровать список транзакций по определенному слову в описании? Да/Нет ")
        answer_user = input("Пользователь: да/нет ").lower()
        if answer_user == "да":
            word = input("Введите параметры поиска ")
            filter_bank_data = operation_search(filter_bank_data, search_word=word)
        print("Программа: Распечатываю итоговый список транзакций...")
        if filter_bank_data:
            print(
                f"""
Программа: 
Всего банковских операций в выборке: {len(filter_bank_data)}"""
            )
            for one_operation in filter_bank_data:
                try:
                    print(
                        f"""
{date_time_formatter(one_operation['date'])} {one_operation['description']}
{bank_data_conversion(one_operation['from'])} -> {bank_data_conversion(one_operation['to'])}
Сумма {one_operation['operationAmount']['amount']} {one_operation['operationAmount']['name']}
"""
                    )
                except Exception:
                    print(
                        f"""
{date_time_formatter(one_operation['date'])} {one_operation['description']}
{bank_data_conversion(one_operation['to'])}
Сумма {one_operation['operationAmount']['amount']} {one_operation['operationAmount']['currency']['name']}"""
                    )


if __name__ == "__main__":
    main()
