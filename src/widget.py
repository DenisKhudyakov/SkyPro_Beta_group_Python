from datetime import datetime

from src.masks import maskin_bil_number, masking_the_card


def bank_data_conversion(bank_data: str) -> str:
    """
    Функиця преобразования банковских данных
    :param bank_data: строка в формате, например Visa Classic 6831982476737658
    :return: строка в формате, например Visa Platinum 7000 79** **** 6361
    """
    bank_data_list = bank_data.split()
    if bank_data.startswith("Счет"):
        return " ".join([bank_data_list[0], maskin_bil_number(bank_data_list[1])]) if bank_data else ""
    elif len(bank_data.split()) >= 3:
        return (
            " ".join(
                [
                    bank_data_list[0],
                    bank_data_list[1],
                    masking_the_card(bank_data_list[2]),
                ]
            )
            if bank_data
            else ""
        )
    return " ".join([bank_data_list[0], masking_the_card(bank_data_list[1])]) if bank_data else ""


def date_time_formatter(data_and_time: str) -> str:
    """
    функцию, которая принимает на вход строку,
    вида "2018-07-11T02:26:18.671407"
    и возвращает строку с датой в виде "11.07.2018"
    :param data_and_time: строковое значение даты и времени
    :return: отформатированная дата
    """
    pattern = "%Y-%m-%dT%H:%M:%S.%f"
    pattern2 = "%Y-%m-%dT%H:%M:%SZ"
    format = "%d.%m.%Y"
    return (
        datetime.strptime(data_and_time, pattern).strftime(format)
        if len(data_and_time) > 20
        else datetime.strptime(data_and_time, pattern2).strftime(format)
    )


if __name__ == "__main__":
    # print(bank_data_conversion("Visa Classic 6831982476737658"))
    print(date_time_formatter("2018-03-23T10:45:06.972075"))
