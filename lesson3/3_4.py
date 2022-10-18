#4.* Задайте список из произвольных вещественных чисел, количество задаёт пользователь.
#Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
#in
#5
#out
#[5.16, 8.62, 6.57, 7.92, 9.22]
#Min: 0.16, Max: 0.92. Difference: 0.76

import random

num = int(input('введите число '))
num_list = []
for i in range(num):
    num_list.append(round(random.uniform(0, 10), 2))

print(num_list)

num_list_rem = []
for i in range(len(num_list)):
    num_list_rem.append(round(num_list[i]%1,2))

# print(num_list_rem) - не обязательно) добавлял для проверки)

a = min(num_list_rem)
b = max(num_list_rem)
c = b-a

print("Min: ", a, " Max: ", b, " difference: ", c)
