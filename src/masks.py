
def masking_the_card(number_card: str) -> str:
    """Преобразование 12ти значного формата карты в замаскированный тип вида: XXXX XX** **** XXXX"""
    return ' '.join([number_card[0:4], number_card[4:6]+'**', '****', number_card[12:16]])


