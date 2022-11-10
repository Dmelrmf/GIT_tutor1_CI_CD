from calcu_func import calcu as cal_111


def test_calcu(a, b):
    c = cal_111(a, b)

    testt_c = a * b

    assert c == testt_c


def test_calcu_two(a, b):
    c = cal_111(a, b)

    test_c = a * b

    assert c != test_c


test_calcu(3, 3)
test_calcu_two('a', 3)