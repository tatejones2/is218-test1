from src.operations import add, subtract, multiply, divide

def test_add():
    assert add(2, 3) == 5

def test_subtract():
    assert subtract(5, 3) == 2

def test_multiply():
    assert multiply(4, 3) == 12

def test_divide():
    assert divide(6, 2) == 3
    try:
        divide(5, 0)
        assert False, "Expected ValueError for division by zero"
    except ValueError:
        pass