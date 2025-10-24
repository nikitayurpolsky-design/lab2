import pytest
from advanced_calculator import AdvancedCalculator

def test_advanced_calculator_add():
    calc = AdvancedCalculator()
    assert calc.add(2, 3) == 5
    assert calc.history == ["2 + 3 = 5"]

def test_advanced_calculator_history():
    calc = AdvancedCalculator()
    calc.add(1, 2)
    calc.subtract(5, 3)
    assert len(calc.get_history()) == 2
    assert calc.get_history()[0] == "1 + 2 = 3"
    assert calc.get_history()[1] == "5 - 3 = 2"

def test_advanced_calculator_clear_history():
    calc = AdvancedCalculator()
    calc.add(1, 2)
    calc.clear_history()
    assert calc.get_history() == []

def test_advanced_calculator_factorial():
    calc = AdvancedCalculator()
    assert calc.factorial(5) == 120
    assert calc.factorial(0) == 1

def test_advanced_calculator_factorial_negative():
    calc = AdvancedCalculator()
    with pytest.raises(ValueError):
        calc.factorial(-1)