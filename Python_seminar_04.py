# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества. 
# m — кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.
from random import randint
def task01():
    countArray1 = int (input("Введите количество элементов первого списка: "))
    countArray2 = int (input("Введите количество элементов второго списка: "))
    
    array1 = [randint(1, countArray1) for i in range(countArray1)]
    array2 = [randint(1, countArray2) for i in range(countArray2)]

    n1 = int(input("Введите количество элементов первого списка: "))
    n2 = int(input("Введите количество элементов второго списка: "))
    array1 = []
    array2 = []
    for i in range(countArray1):
        array1.append(int(input("Введите элемент первого списка: ")))
    for j in range(countArray2):
        array2.append(int(input("Введите элемент второго списка: ")))
    array3 = []
    for i in array1:
        if i in array2 and i not in array3:
                array3.append(i)
    array3.sort()
    print(f"Числа из двух наборов, выведенные последовательно: {array3}")


# Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. Она растёт на круглой грядке, причём кусты высажены только по окружности. 
# Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растёт N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное число ягод — на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники. 
# Эта система состоит из управляющего модуля и нескольких собирающих модулей. 
# Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, 
# которое может собрать за один заход собирающий модуль, находясь перед некоторым кустом заданной во входном файле грядки.

def task01():
    numberBushes = int(input("Введите количество кустов: "))
    arrayBerryes = list(randint(0, 10) for i in range(numberBushes))
    resultArray = []
    count = 0
    summa = 0

    print(arrayBerryes)

    while (count < numberBushes):
        if (count == numberBushes - 1):
            summa = arrayBerryes[count] + arrayBerryes[count - 1] + arrayBerryes[0]
        else:
            summa = arrayBerryes[count] + arrayBerryes[count - 1] + arrayBerryes[count + 1]
            resultArray.append(summa)
            resultArray.sort()
        count += 1

    print(f"Максимальное число ягод за однин проход {resultArray[-1]}")

    
task01()
task02()