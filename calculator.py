class Calculator:
    """Простой калькулятор для демонстрации CI/CD"""
    
    def add(self, a, b):
        """Сложение двух чисел"""
        return a + b
        
    def subtract(self, a, b):
        """Вычитание двух чисел"""
        return a - b
        
    def multiply(self, a, b):
        """Умножение двух чисел"""
        return a * b
        
    def divide(self, a, b):
        """Деление двух чисел"""
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b
        
    def power(self, a, b):
        """Возведение в степень"""
        return a ** b