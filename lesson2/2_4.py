#4. Напишите программу, которая принимает на вход 2 числа. Задайте список из N элементов, 
#заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях(не индексах).
#Position one: 1
#Position two: 3
#Number of elements: 5
#-> [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
#-> 15

import numbers


n = int(input('введите число, я сделаю список от его минуса до самого числа '))

numbers = list(range(-n,n+1))
print(numbers)

c = n*2+1 #размер списка
a = int(input('теперь введите позицию первого числа, потом мы его умножим на второе '))
b = int(input('теперь введите позицию второго числа, потом мы его умножим на первое '))

g = numbers[a-1]*numbers[b-1]
print('произведение ', a, ' элемента и ', b, ' элемента =', g)
