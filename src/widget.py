from datetime import datetime

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(account_info: str) -> str:
    """Функция общей маскировки карты и счета"""

    account_number = account_info[account_info.rfind(" ") + 1 :]

    if "Счет" in account_info:
        return (
            account_info[: account_info.rfind(" ")]
            + " "
            + get_mask_account(account_number)
        )
    else:
        return (
            account_info[: account_info.rfind(" ")]
            + " "
            + get_mask_card_number(account_number)
        )


def get_data(date: str) -> str:
    """Функция преобразования даты"""

    date_update = datetime.strptime(date, "%Y-%m-%dT%H:%M:%S.%f")
    return date_update.strftime("%d.%m. %Y")
