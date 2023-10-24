from datetime import datetime

from masks import maskin_bil_number, masking_the_card


def bank_data_conversion(bank_data: str) -> str:
    """
    Функиця преобразования банковских данных
    :param bank_data: строка в формате, например Visa Platinum 7000 7922 8960 6361
    :return: строка в формате, например Visa Platinum 7000 79** **** 6361
    """
    bank_data_list = bank_data.split()
    if bank_data.startswith("Счет"):
        return ' '.join([bank_data_list[0], maskin_bil_number(bank_data_list[1])])
    return ' '.join([bank_data_list[0], masking_the_card(bank_data_list[1])])


def date_time_formatter(data_and_time: str) -> str:
    """
    функцию, которая принимает на вход строку,
    вида "2018-07-11T02:26:18.671407"
    и возвращает строку с датой в виде "11.07.2018"
    :param data_and_time:
    :return:
    """
    pattern = '%Y-%m-%dT%H:%M:%S'
    return datetime.strptime(data_and_time[:-7], pattern).strftime('%d.%m.%Y')



