#2. Напишите программу, которая найдёт произведение пар чисел списка.
#Парой считаем первый и последний элемент, второй и предпоследний и т.д.
#in
#4
#out
#[2, 5, 8, 10]
#[20, 40]
#in
#5
#out
#[2, 2, 4, 8, 8]
#[16, 16, 4]

from random import randint


num = int(input('введите число '))
num_list = []
for i in range(num):
    num_list.append(randint(-10, 10))

print(num_list)

num_list_result = []

for i in range((len(num_list)+1)//2):
    if (i != (len(num_list)-1-i)):
        num_list_result.append(num_list[i]*num_list[len(num_list)-1-i])
    else:
        num_list_result.append(num_list[i])
print(num_list_result)
