from calcu_func import calcu as cal_111


def test_calcu(a=str, b=int):
    c = cal_111(a=str, b=int)

    testt_c = a * b

    assert c == testt_c


def test_calcu_two(a=str, b=int):
    c = cal_111(a=str, b=int)

    test_c = a * b

    assert c != test_c


test_calcu('a', 3)
test_calcu_two(3, 3)