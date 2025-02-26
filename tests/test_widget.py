import pytest

from src.widget import get_date, mask_account_card


@pytest.mark.parametrize(
    "value",
    [
        ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
        ("Mastercard 1234567890123456", "Mastercard 1234 56** **** 3456"),
        ("Мир 2200123456789010", "Мир 2200 12** **** 9010"),
        ("Union Pay 6010203040506070", "Union Pay 6010 20** **** 6070"),
        ("Счет 73654108430135874305", "Счет **4305"),
        ("7000792289606361", "7000 79** **** 6361"),
        ("73654108430135874305", "**4305"),
    ],
)
def test_mask_account_card(value):
    assert mask_account_card(value)


@pytest.mark.parametrize(
    "value",
    [
        ("Visa Platinum ", "номер карты не указан"),
        ("Счет ", "номер счета не указан"),
        ("", "нет данных"),
        ("1", "некорректный номер карты"),
    ],
)
def test_mask_account_card_valueerror(value):
    with pytest.raises(ValueError):
        mask_account_card(value)


def test_mask_account_card_valueerror():
    with pytest.raises(ValueError):
        mask_account_card("")


def test_get_date_valueerror():
    with pytest.raises(ValueError):
        get_date("")
