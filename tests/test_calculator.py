import pytest
from calculator import Calculator

def test_calculator_add():
    """Тест сложения калькулятора"""
    calc = Calculator()
    assert calc.add(2, 3) == 5
    assert calc.add(-1, 1) == 0
    assert calc.add(0, 0) == 0

def test_calculator_subtract():
    """Тест вычитания калькулятора"""
    calc = Calculator()
    assert calc.subtract(5, 3) == 2
    assert calc.subtract(0, 5) == -5

def test_calculator_multiply():
    """Тест умножения калькулятора"""
    calc = Calculator()
    assert calc.multiply(4, 3) == 12
    assert calc.multiply(0, 5) == 0

def test_calculator_divide():
    """Тест деления калькулятора"""
    calc = Calculator()
    assert calc.divide(10, 2) == 5
    assert calc.divide(5, 2) == 2.5

def test_calculator_divide_by_zero():
    """Тест деления на ноль"""
    calc = Calculator()
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        calc.divide(5, 0)

def test_calculator_power():
    """Тест возведения в степень"""
    calc = Calculator()
    assert calc.power(2, 3) == 8
    assert calc.power(5, 0) == 1