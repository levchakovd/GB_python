#3. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
#Без использования встроенной функции преобразования, без строк.
#in
#88
#out
#1011000
#in
#11
#out
#1011

#a = int(input('Введите число, чтобы я преобразовал его в двоичное: '))
#print('{0:b}'.format(a))
#type = str - не подходит значит(



def conv_bin(num: int):
    list_nums = []

    while num > 0:
        list_nums.insert(0, num%2)
        num //=2

    print(*list_nums, sep='')

conv_bin(int(input('Введите число, чтобы я преобразовал его в двоичное: ')))