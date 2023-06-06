# Задача 26:  Напишите программу, которая на вход принимает два числа A и B, 
# и возводит число А в целую степень B с помощью рекурсии.

# *Пример:*

# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8 

def task01():
    number = int (input("Введите число: "))
    powOfNumber = int (input("Введите число: "))

    def newPow(number, powOfNumber):
        if powOfNumber==0:
           return 1
        return number*(newPow(number, powOfNumber-1))
    print(f"{number} в степени {powOfNumber} равно {newPow(number, powOfNumber)}")

# Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. 
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.

# *Пример:*

# 2 2
#     4 

def task02():
    number1 = int (input("Введите первое число: "))
    number2 = int (input("Введите второе число: "))
    
    def summ(number1, number2):
        if number1==0:
            return number2
        else:
            return summ(number1-1, number2+1)
    print (f"Сумма {number1} и {number2} равна {summ(number1, number2)}")