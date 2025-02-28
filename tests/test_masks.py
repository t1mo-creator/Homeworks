import pytest
from src.masks import get_mask_card_number
from src.masks import get_mask_account


def test_get_mask_card_numbers(numbers_16):
    assert get_mask_card_number(numbers_16) == "7000 79** **** 6361"

def test_get_mask_card_numbers_with_spaces(numbers_16_spases):
    assert get_mask_card_number(numbers_16_spases) == "7000 79** **** 6361"

def test_get_mask_account(numbers_20):
    assert get_mask_account(numbers_20) == "**1234"
