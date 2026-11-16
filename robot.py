MENU = {"아메리카노": 4500, "라떼": 5000, "샌드위치": 6500}
DISCOUNT_MIN = 20000
DISCOUNT_MIN_PER = 10
DISCOUNT_MAX = 50000
DISCOUNT_MAX_PER = 20
BASE_FEE = 2000
BASE_KM = 2
EXTRA_FEE_PER_KM = 500
MAX_FEE = 5000
LONG_DIST = 8
SHORT_DIST = 5

# def order_total(items):
#     total = 0
#     for name in items:
#         if name not in MENU:
#             raise ValueError("없는 메뉴입니다: " + name)
#         total += MENU[name]
#     if total >= DISCOUNT_MIN:
#         total = total - total//DISCOUNT_PER
#     return total

def order_total(items):
    total = 0
    total_value = 0
    for key, value in items.items():
        if value > 0:
            total_value += value
            if total_value > 10:
                raise ValueError("10개를 초과할 수 없습니다.")
            if key not in MENU:
                raise ValueError("없는 메뉴입니다: " + key)
            total += MENU[key] * value
        else:
            raise ValueError("1보다 낮은 수 만큼은 받을 수 없습니다.")
    if total >= DISCOUNT_MAX:
        total = total - total//DISCOUNT_MAX_PER
    elif total >= DISCOUNT_MIN:
        total = total - total//DISCOUNT_MIN_PER
    return total

def delivery_fee(km):
    if km < 0:
        raise ValueError("거리는 0 이상이어야 합니다.")
    if km > BASE_KM:
        km -= BASE_KM
        if BASE_FEE + km*EXTRA_FEE_PER_KM > MAX_FEE:
            return MAX_FEE
        else:
            return BASE_FEE + km*EXTRA_FEE_PER_KM
    return BASE_FEE

def apply_coupon(total, code):
    _total = total

    if code == []:
        return total
    for cop in code:
        if cop == "HALF":
            # _total -= min(total//2 , 5000)
            _total = min(_total, total-min(total//2 , 5000))
        elif cop == "WELCOME":
            _total = min(_total, max(total-3000, 0))
        elif cop != "HALF" and cop != "WELCOME":
            raise ValueError("유효한 쿠폰이 아닙니다.")
    return _total

def can_deliver(battery, distance_km, load_kg):
    _distance_km = distance_km * 2
    if load_kg <= 10:
        _distance_km *= SHORT_DIST
    else:
        _distance_km *= LONG_DIST
    if battery - _distance_km >= 20:
        return True
    else:
        return False