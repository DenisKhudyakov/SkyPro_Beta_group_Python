import logging
from typing import Any


def setup_logging() -> Any:
    """
    Функция записи информации в файл
    :return: логи информации
    """
    logger = logging.getLogger(__name__)
    file_handler = logging.FileHandler("data_collection.log", "w")
    file_formatter = logging.Formatter("%(asctime)s %(funcName)s %(levelname)s: %(message)s")
    file_handler.setFormatter(file_formatter)
    logger.addHandler(file_handler)
    logger.setLevel(logging.INFO)
    return logger


def setup_error_logging() -> Any:
    """
    Функция записи ошибок в файл
    :return: логи ошибок
    """
    logger = logging.getLogger(__name__)
    file_handler = logging.FileHandler("data_collection.log", "w")
    file_formatter = logging.Formatter("%(asctime)s %(funcName)s %(levelname)s: %(message)s")
    file_handler.setFormatter(file_formatter)
    logger.addHandler(file_handler)
    logger.setLevel(logging.ERROR)
    return logger
