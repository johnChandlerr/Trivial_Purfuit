import pytest

'''
pytest -vv

pytest -vv test.py

pytest --durations=0 test.py

pytest -vv -m group
'''

def func(x):
    if x == 0:
        raise ValueError("value error")
    else:
        pass


def test_fun1():
    with pytest.raises(ValueError):
        func(0)


def test_fun2():
    assert func(1) is None


def add(x, y):
    return x + y


@pytest.mark.parametrize(
    "x, y, expected",
    [
        (2, 3, 5),
        (2, 2, 4),
        (18, 20, 38),
    ]
)
def test_add(x, y, expected):
    assert add(x, y) == expected
