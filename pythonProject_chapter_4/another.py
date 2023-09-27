try:
    number1 = int(input("Введите первое число: "))
    number2 = int(input("Введите второе число: "))
    print("Результат деления:", number1/number2)
except ZeroDivisionError:
    print("Попытка деления числа на ноль")
print("Завершение программы")