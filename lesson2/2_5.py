#** Реализуйте алгоритм перемешивания списка. Без функции shuffle из модуля random.
10
#-> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#-> [0, 7, 6, 3, 4, 2, 9, 5, 1, 8]

from random import sample

num = int(input())
num_list = list(range(num))

print(num_list)

shuf_list = sample(num_list, num)

print(shuf_list)