#1. Задайте список, состоящий из произвольных чисел, количество задаёт пользователь.
#Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётных позициях(не индексах).
#in 5
# out
#[10, 2, 3, 8, 9]
#22

from random import randint

num = int(input('введите число '))
num_list = []
for i in range(num):
    num_list.append(randint(-10, 10))

print(num_list)

result = 0

for i in range(0, num, 2):
    result += num_list[i]

print(result)

