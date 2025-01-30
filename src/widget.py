from src.mask import get_mask_account, get_mask_card_number


def mask_account_card(payment: str) -> str:
    """Определяем счет или номер карты и тип самой карты."""
    name, number = payment.rsplit(' ', maxsplit=1)
    if len(number) == 16:
        masked_number = get_mask_card_number(number)
    elif len(number) == 20:
        masked_number = get_mask_account(number)
    else:
        raise ValueError('Invalid payment')

    return f'{name} {masked_number}'

def get_date(user_data: str) -> str:
    """Функция, которая изменяет формат даты"""
    data_day = user_data.split("Т")[0]
    return f"{(user_data[8:10])}.{(data_day.split('-')[-2])}.{(data_day.split('-')[-3])}"

card = "Maestro 8990922113665229"
masked_info = get_mask_card_number(card)