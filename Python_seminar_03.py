# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
# 5    1 2 3 4 5
#     3
#     -> 1
from random import randint
def task01():
    listcounttask1 = int (input("Введите длину списка: "))
    listtask1 = [randint(1, listcounttask1) for i in range(listcounttask1)]
    #print (listtask1)
    numbertask1 = int (input("Введите число: "))
    count=listtask1.count(numbertask1)
    if count>0:
        print (f"Число {numbertask1} в списке повторяется {count} раз")
    else:
        print ("Такого числа нет в списке")
    
# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
# 5
#     1 2 3 4 5
#     6
#     -> 5
def task02():
    listcounttask2 = int (input("Введите длину списка: "))
    listtask2 = [randint(1, 20) for i in range(listcounttask2)]
    #print(listtask2)
    numbertask2 = int (input("Введите число: "))
    indexValue=0
    minValue = abs(numbertask2 - listtask2[0])
    for i in range(1, listcounttask2):
        tempValue = abs(numbertask2 -listtask2[i])
        if tempValue < minValue:
            minValue = tempValue
            indexValue=i
    print(f"Самый близкий по величине элемент к числу {numbertask2} — это {listtask2[indexValue]}")
    
# *Задача 20: * В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность. 
# В случае с английским алфавитом очки распределяются так:
# A, E, I, O, U, L, N, S, T, R – 1 очко; D, G – 2 очка; B, C, M, P – 3 очка; F, H, V, W, Y – 4 очка; 
# K – 5 очков; J, X – 8 очков; Q, Z – 10 очков. 
# А русские буквы оцениваются так: А, В, Е, И, Н, О, Р, С, Т – 1 очко; Д, К, Л, М, П, У – 2 очка; Б, Г, Ё, Ь, Я – 3 очка; Й, Ы – 4 очка; 
# Ж, З, Х, Ц, Ч – 5 очков; Ш, Э, Ю – 8 очков; Ф, Щ, Ъ – 10 очков. Напишите программу, которая вычисляет стоимость введенного пользователем слова. 
# Будем считать, что на вход подается только одно слово, которое содержит либо только английские, либо только русские буквы.
# ноутбук
#     12
def task03():
    word = input("Введите слово: ").upper()
    count=0
    alphabet={
    1:'AEIOULNSTRАВЕИНОРСТ',
    2:'DGДКЛМПУ',
    3:'BCMPБГЁЬЯ',
    4:'FHVWYЙЫ',
    5:'KЖЗХЦЧ',
    8:'JXШЭЮ',
    10:'QZФЩЪ'}
    for i in word:
        for key, value in alphabet.items():
            if i in value:
                count=count+key
    print (f"Цена слова {word} равна {count}")
    
task01()
task02()
task03()