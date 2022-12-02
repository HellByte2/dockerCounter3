def inc(x):
    return x + 1


def test_1():
    assert inc(3) == 4


def test_2():
    assert inc(4) == 5


def test_3():
    assert inc(0) == 1
