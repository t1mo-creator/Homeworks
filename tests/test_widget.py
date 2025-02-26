import pytest

from src.widget import get_date, mask_account_card


def test_mask_account_card(value):
    assert mask_account_card(value)


def test_mask_account_card_valueerror(value):
    with pytest.raises(ValueError):
        mask_account_card(value)


def test_get_date(value):
    assert get_date(value)


def test_get_date_valueerror(value):
    with pytest.raises(ValueError):
        get_date(value)
