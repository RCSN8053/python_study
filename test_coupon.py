import pytest

from robot import apply_coupon


def test_only_one_coupon_is_used():
    assert apply_coupon(10000, ["WELCOME", "HALF"]) == 5000


def test_half_coupon_keeps_its_cap():
    assert apply_coupon(30000, ["WELCOME", "HALF"]) == 25000


def test_welcome_can_be_better():
    assert apply_coupon(4000, ["WELCOME", "HALF"]) == 1000


def test_price_can_be_zero():
    assert apply_coupon(2000, ["WELCOME", "HALF"]) == 0


def test_empty_candidates_keep_original_price():
    assert apply_coupon(10000, []) == 10000


def test_lowercase_coupon_is_allowed():
    assert apply_coupon(10000, ["WELCOME"]) == 7000


def test_candidate_order_does_not_change_price():
    assert apply_coupon(10000, ["WELCOME", "HALF"]) == 5000
    assert apply_coupon(10000, ["HALF", "WELCOME"]) == 5000


def test_unknown_coupon_is_checked_even_after_zero():
    with pytest.raises(ValueError):
        apply_coupon(2000, ["WELCOME", "FREE"])