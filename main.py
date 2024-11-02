"""Написать программу, которая:
- Создаёт с помощью генератора списков, список случайных целых чисел от **-50** до **50** размером **25** элементов.
- Находит количество положительных, отрицательных и нулевых элементов в списке.
- Выводит значения и их (*положительных, отрицательных и нулевых*) количество вместе с процентом от общего количества.
- Выводит самое большое и самое маленькое значение"""
import random
numbers=[]
for i in range(25):
    numbers.append(random.randint(-50, 50))
print()
print("Ваш список: ", numbers)
print()

countP=0
positiveNumb=[]
countN=0
negativeNumb=[]
countZ=0
zeros=[]
for i in numbers:
    if i>0:
        countP+=1
        positiveNumb.append(i)
    elif i==0:
        countZ+=1
        zeros.append(i)
    else:
        countN+=1
        negativeNumb.append(i)

print("Положительные элементы: ", positiveNumb)
print("Их кол-во: ", countP)
print("Процент от общего кол-ва: ", countP/25*100)
print()
print("Отрицательные элементы: ", negativeNumb)
print("Их кол-во: ", countN)
print("Процент от общего кол-ва: ", countN/25*100)
print()
print("Нули: ", zeros)
print("Их кол-во: ", countZ)
print("Процент от общего кол-ва: ", countZ/25*100)
print()

min=0
max=0
for i in numbers:
    if i>max:
        max=i
for i in numbers:
    if i<min:
        min=i
print("Максимальное значение: ", max)
print("Минимальное значение: ", min)
print()