from functools import reduce

from masks import maskin_bil_number, masking_the_card


def bank_data_conversion(bank_data: str) -> str:
    """
    :param bank_data: строка в формате, например Visa Platinum 7000 7922 8960 6361
    :return: строка в формате, например Visa Platinum 7000 79** **** 6361
    """
    if bank_data.startswith("Счет"):
        return reduce(
            lambda bill, bil_number: f"{bill} {maskin_bil_number(bill_number=bil_number)}", bank_data.split()
        )
    return reduce(
        lambda typing_card, card_number: f"{typing_card} {masking_the_card(number_card=card_number)}",
        bank_data.split(),
    )
