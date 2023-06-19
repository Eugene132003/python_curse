# Задача 30:  Заполните массив элементами арифметической прогрессии. 
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. 
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.
def task01():
    firstNumberArray = int (input("Введите первый элемент списка: "))
    disArray=int(input("Введите разность элементов списка:"))
    lengthArray = int (input("Введите количество элементов списка: "))
    resultArray = [firstNumberArray + (i - 1) * disArray for i in range(1, lengthArray + 1)]
    print(*resultArray)

# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)
from random import randint
def task02():
    listcount = [randint(-50, 50) for i in range(20)]
    minNumber = int(input("Введите минимум диапозона: "))
    maxNumber = int(input("Введите максимум диапозона: "))
    for i in range(len(listcount)):
        if minNumber <= listcount[i] <= maxNumber:
            print(i)


task01()
task02()