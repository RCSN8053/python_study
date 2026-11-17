from robot import order_total
import pytest


def test_small_order_has_no_discount():
    assert order_total({"아메리카노" : 1, "라떼" : 1}) == 9500


def test_big_order_gets_discount():
    assert order_total({"샌드위치" : 3,"라떼" : 1}) == 22050


def test_exactly_20000_gets_discount():
    assert order_total({"라떼": 4}) == 18000

    
def test_empty_order_is_zero():
    assert order_total({}) == 0


def test_five_lattes_get_one_discount():
    assert order_total({"라떼" : 5}) == 22500


def test_five_sandwiches_get_one_discount():
    assert order_total({"샌드위치" : 5}) == 29250


def test_item_order_does_not_change_price():
    assert order_total({"라떼" : 4, "샌드위치" : 1}) == 23850
    assert order_total({"샌드위치" : 1, "라떼": 4}) == 23850

def test_unknown_menu_raises_error():
    with pytest.raises(ValueError):
        order_total({"콜라" : 1})

def test_11_menu():
    with pytest.raises(ValueError):
        order_total({"라떼" : 11})

def test_11_menu_():
    with pytest.raises(ValueError):
        order_total({"라떼" : 6, "샌드위치": 5})

def test_minus_menu():
    with pytest.raises(ValueError):
        order_total({"라떼" : -3})
def test_menu_zero():
    with pytest.raises(ValueError):
        order_total({"라떼" : 0})


def test_normal_order():
    """할인 기준 미만의 정상 주문 테스트 (< 20,000원)"""
    items = {"아메리카노": 3}  # 4500 * 3 = 13500원
    assert order_total(items) == 13500


def test_min_discount_order():
    """최소 할인 기준 이상 주문 테스트 (20,000원 이상 ~ 50,000원 미만)"""
    # 샌드위치 4개 = 26000원
    # 26000 - (26000 // 10) = 26000 - 2600 = 23400원
    items = {"샌드위치": 4}
    expected_total = 26000 - (26000 // 10)
    assert order_total(items) == expected_total


def test_max_discount_order():
    """최대 할인 기준 이상 주문 테스트 (50,000원 이상)"""
    # 샌드위치 8개 = 52000원
    # 52000 - (52000 // 20) = 52000 - 2600 = 49400원
    items = {"샌드위치": 8}
    expected_total = 52000 - (52000 // 20)
    assert order_total(items) == expected_total


@pytest.mark.parametrize(
    "invalid_items, expected_message",
    [
        ({"아메리카노": 0}, "1보다 낮은 수 만큼은 받을 수 없습니다."),
        ({"라떼": -1}, "1보다 낮은 수 만큼은 받을 수 없습니다."),
        ({"아메리카노": 11}, "10개를 초과할 수 없습니다."),
        ({"떡볶이": 1}, "없는 메뉴입니다: 떡볶이"),
    ]
)
def test_order_exceptions(invalid_items, expected_message):
    """잘못된 입력값에 따른 예외(ValueError) 및 메시지 검증 (parametrize 활용)"""
    with pytest.raises(ValueError) as exc_info:
        order_total(invalid_items)
    assert str(exc_info.value) == expected_message