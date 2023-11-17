from typing import Any

from src.logger import setup_error_logging, setup_logging

logging = setup_logging()
logging_error = setup_error_logging()


def masking_the_card(number_card: str) -> str | Any:
    """
    Преобразование 12ти значного формата карты в замаскированный тип вида: XXXX XX** **** XXXX
    :param num_card: Номер для маскирования
    :return: Маскированный по правилу номер
    """
    logging.info("Запустилась функция форматирования банковской карты")
    return (
        " ".join([number_card[0:4], number_card[4:6] + "**", "****", number_card[12:16]])
        if len(number_card) == 12
        else logging.error("Осторожно введен некорректный номер")
    )


def maskin_bil_number(bill_number: str) -> str:
    """
    Пример работы функции, возвращающей маску счета
    73654108430135874305  # входной аргумент
    **4305  # выход функции
    """
    logging.info("Запустилась функция форматирования банковского счета")
    return "".join(["**", bill_number[-4:]]) if bill_number else ""
