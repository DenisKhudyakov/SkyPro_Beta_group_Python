def masking_the_card(number_card: str) -> str:
    """
    Преобразование 12ти значного формата карты в замаскированный тип вида: XXXX XX** **** XXXX
    :param num_card: Номер для маскирования
    :return: Маскированный по правилу номер
    """
    return " ".join([number_card[0:4], number_card[4:6] + "**", "****", number_card[12:16]]) if number_card else ""


def maskin_bil_number(bill_number: str) -> str:
    """
    Пример работы функции, возвращающей маску счета
    73654108430135874305  # входной аргумент
    **4305  # выход функции
    """
    return "".join(["**", bill_number[-4:]]) if bill_number else ""
