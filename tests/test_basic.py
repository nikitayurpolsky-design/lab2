def test_addition():
    """Тест сложения"""
    assert 1 + 1 == 2

def test_subtraction():
    """Тест вычитания"""
    assert 5 - 3 == 2

def test_multiplication():
    """Тест умножения"""
    assert 2 * 3 == 6

def test_division():
    """Тест деления"""
    assert 10 / 2 == 5

def test_string_operations():
    """Тест строковых операций"""
    assert "hello".upper() == "HELLO"
    assert "WORLD".lower() == "world"