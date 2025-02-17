from src.masks import get_mask_account, get_mask_card_number
import pytest


def test_get_mask_card_number():
    assert get_mask_card_number("7000792289606361") == "7000 79** **** 6361"
    assert get_mask_card_number("800079228960636") == "Неверный формат банковской карты"


def test_get_mask_account():
    assert get_mask_account("73654108430135874305") == "**4305"
    assert get_mask_account("786541084301358743") == "Неверный формат номера счета"


@pytest.mark.parametrize("x", [7000792289606361, 8000522289606361, 700792289606361, ()])
def test_get_mask_card_number(x):
    card_number_str = str(x)
    assert f"{card_number_str[:4]} {card_number_str[4:6]}** **** {card_number_str[-4:]}"


@pytest.mark.parametrize("x", [73654108430135874305, 773654108430135874305, 3373654108430135874305, ()])
def test_get_mask_account(x):
    account_number_str = str(x)
    assert f"**{account_number_str[-4:]}"
