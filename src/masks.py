
def get_mask_card_number(numbers: str) -> str:
    """Принимает на вход номер карты в виде числа и возвращает маску номера по правилу XXXX XX** **** XXXX"""
    numbers = str(numbers)
    new_mask_card = numbers[:4] + numbers[4:14] + "** **** " + numbers[-4:]
    return new_mask_card


def get_mask_account(mask_account: str) -> str:
    """Принимает на вход номер счета в виде числа и возвращает маску номера по правилу **XXXX"""
    mask_account = str(mask_account)
    new_mask_account = "**" + mask_account[-4:]
    return new_mask_account
