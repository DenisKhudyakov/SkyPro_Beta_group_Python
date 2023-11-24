# маскировка номеров карт и счетов
from src.masks import maskin_bil_number, masking_the_card
# маскировка строки с номером в зависимости от типа (Счет или карта)
from src.widget import bank_data_conversion
# фильтровка списка транзакций по статусу (статус передается параметром),
# сортировка по дате списка транзакций с указанием направления сортировки (по возрастанию/по убыванию)
from src.processing import filter_operations, sorted_operation
# 1) функция-генератор с сортировкой списка транзакций по валюте
# 2) функция-генератор возвращающая описание каждой операции из списка транзакций
# 3) генератор номеров карт в заданном диапазоне
from src.generators import filter_by_currency, transaction_descriptions, card_number_generator
# функция чтения json файла
from src.utils import get_json
# функция чтения csv файла, функция чтения excel файла
from src.read_the_table import read_xlsx_csv_file
# функция поиска операций с определенными словами в описании
# функция подсчета количества операций определенной категории
from src.processing import operation_search, operation_counter

def main():
    while True:
        print("""
Программа: Привет! Добро пожаловать в программу работы с банковскими транзакициями. 
Выберите необходимый пункт меню:
1. Получить информацию о транзакциях из json файла
2. Получить информацию о транзакциях из csv файла
3. Получить информацию о транзакциях из xlsx файла
Для выхода нажмите "q"
""")
        answer_user = input('Пользователь: ')
        match answer_user:
            case '1':
                print('читаем json')
            case '2':
                print('Читаем csv')
            case '3':
                print('читаем xlsx')
            case 'q':
                print('Приложение завершается')
                break


if __name__ == "__main__":
    main()
