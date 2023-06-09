# Задача 2: Найдите сумму цифр трехзначного числа.
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)
def task01():
    value = int (input ("Введите трехзначное число: "))
    if (value >= 100 and value <= 999):
        valueForPrint=value
        summ = 0
        for number in [100,10,1]:
            summ=summ+value//number
            value %= number
        print (f"Сумма всех трех цифр числа {valueForPrint} равна {summ}")
    else: print("Число НЕ трехзначное")


# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов.
# Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа 
# сделали одинаковое количество журавликов, а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
# 6 -> 1  4  1
# 24 -> 4  16  4
# 60 -> 10  40  10

def task02():
    valueAll = int (input ("Введите общее количество журавликов: "))
    if (valueAll%6==0):
        valPetrSerg=int(valueAll/6)
        valKate=int(valPetrSerg*4)
        print (f"Петя и Сережа сделали по {valPetrSerg} журавликов, а Катя сделала {valKate} журавликов.")
    else: print ("Не могли они столько журавликов сделать!")


# Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались 
# за проезд и получали билет с номером. Счастливым билетом называют такой билет с 
# шестизначным номером, где сумма первых трех цифр равна сумме последних трех. Т.е. билет с номером 385916 – счастливый, 
# т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.
# 385916 -> yes
# 123456 -> no

def task03():
    numberFull =int( input ("Введите номер билета: "))
    def summ(valuesumm):
        summTicket = 0
        for numTicket in [100,10,1]:
            summTicket=summTicket+valuesumm//numTicket
            valuesumm %= numTicket
        return summTicket
    if (numberFull >= 100000 and numberFull<= 999999):
        if (summ(int(str(numberFull)[:3]))==summ(int(str(numberFull)[-3:]))):
            print(f"Билет с номером {numberFull} - счастливый! Можете съесть!")
        else: print (f"Билет с номером {numberFull} - НЕсчастливый!, лузер!")
    else: print ("Это не номер билета, неудачник!")

# Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, 
# если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).
# 3 2 4 -> yes
# 3 2 1 -> no

def task04():
    lengthShoko =int( input ("Введите длину шоколадки: "))
    widthShoko =int( input ("Введите ширину шоколадки: "))
    cutShoko =int( input ("Введите количество долек: "))
    
    if (lengthShoko<widthShoko):
        temp=lengthShoko
        lengthShoko=widthShoko
        widthShoko=temp
        
    if ((cutShoko%lengthShoko==0 or cutShoko%widthShoko==0) and lengthShoko*widthShoko>cutShoko):
        print ("Да, вроде, разделится")
        
    else: print ("Не делись, кушай так!")

task01()
task02()
task03()
task04()