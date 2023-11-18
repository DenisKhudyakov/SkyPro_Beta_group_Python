from src.masks import maskin_bil_number, masking_the_card


def test_masking_the_card() -> None:
    """
    Тестовая функция для поверки преобразования банковской карты
    :return: Тестовая фукнция ничего не возвращает
    """
    assert masking_the_card("7000792289606361") == "7000 79** **** 6361"
    assert masking_the_card("") is None


def test_maskin_bil_number() -> None:
    """
    Тестовая функция для проверки преобразования банковского счета
    :return: Тестовая фукнция ничего не возвращает
    """
    assert maskin_bil_number("73654108430135874305") == "**4305"
    assert maskin_bil_number("") == ""
