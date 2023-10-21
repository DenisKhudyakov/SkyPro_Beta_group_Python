
def masking_the_card(number_card: str) -> str:
    """
    Преобразование 12ти значного формата карты в замаскированный тип вида: XXXX XX** **** XXXX
    :param num_card: Номер для маскирования
    :return: Маскированный по правилу номер
    """
    return ' '.join([number_card[0:4], number_card[4:6]+'**', '****', number_card[12:16]])


