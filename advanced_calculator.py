class AdvancedCalculator:
    """Расширенный калькулятор с дополнительными функциями"""
    
    def __init__(self):
        self.history = []
    
    def add(self, a, b):
        result = a + b
        self.history.append(f"{a} + {b} = {result}")
        return result
        
    def subtract(self, a, b):
        result = a - b
        self.history.append(f"{a} - {b} = {result}")
        return result
        
    def multiply(self, a, b):
        result = a * b
        self.history.append(f"{a} * {b} = {result}")
        return result
        
    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        result = a / b
        self.history.append(f"{a} / {b} = {result}")
        return result
    
    def power(self, a, b):
        result = a ** b
        self.history.append(f"{a} ^ {b} = {result}")
        return result
        
    def get_history(self):
        return self.history
        
    def clear_history(self):
        self.history = []
        
    def factorial(self, n):
        if n < 0:
            raise ValueError("Factorial is not defined for negative numbers")
        if n == 0:
            return 1
        result = 1
        for i in range(1, n + 1):
            result *= i
        self.history.append(f"{n}! = {result}")
        return result
    def percentage(self, value, percent):
        """Вычисление процента от числа"""
        result = value * (percent / 100)
        self.history.append(f"{percent}% от {value} = {result}")
        return result
        
    def square_root(self, n):
        """Вычисление квадратного корня"""
        if n < 0:
            raise ValueError("Cannot calculate square root of negative number")
        result = n ** 0.5
        self.history.append(f"√{n} = {result}")
        return result