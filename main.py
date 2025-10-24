def main():
    print("🧮 Демонстрация работы калькуляторов")
    
    # Простой калькулятор
    print("\n=== Простой калькулятор ===")
    simple_calc = Calculator()
    print(f"2 + 3 = {simple_calc.add(2, 3)}")
    print(f"5 - 3 = {simple_calc.subtract(5, 3)}")
    print(f"4 * 3 = {simple_calc.multiply(4, 3)}")
    print(f"10 / 2 = {simple_calc.divide(10, 2)}")
    
    # Продвинутый калькулятор
    print("\n=== Продвинутый калькулятор ===")
    advanced_calc = AdvancedCalculator()
    print(f"2 + 3 = {advanced_calc.add(2, 3)}")
    print(f"5 ^ 2 = {advanced_calc.power(5, 2)}")
    print(f"5! = {advanced_calc.factorial(5)}")
    print(f"10% от 200 = {advanced_calc.percentage(200, 10)}")
    print(f"√25 = {advanced_calc.square_root(25)}")
    
    print("\n=== История операций ===")
    for operation in advanced_calc.get_history():
        print(operation)

if __name__ == "__main__":
    main()