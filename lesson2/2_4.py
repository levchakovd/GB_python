#4. Напишите программу, которая принимает на вход 2 числа. Задайте список из N элементов, 
#заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях(не индексах).
#Position one: 1
#Position two: 3
#Number of elements: 5
#-> [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
#-> 15

import numbers

num = input('введите число, я сделаю список от его минуса до самого числа ')

numbers = list(range(-num,num+1))
print(numbers)

c = num*2+1 #размер списка
a = int(input('теперь введите позицию первого числа, потом мы его умножим на второе '))
b = int(input('теперь введите позицию второго числа, потом мы его умножим на первое '))

while (a > c or b > c or a < 1 or b < 1):
    print('это не будет работать')
    a = int(input('первое число! снова! у тебя получится '))
    b = int(input('второе число! снова! у тебя получится '))
    
g = numbers[a-1]*numbers[b-1]
print('произведение ', a, ' элемента и ', b, ' элемента =', g)
