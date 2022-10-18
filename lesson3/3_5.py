#5. ** Задайте число. Составьте список чисел Фибоначчи, 
# в том числе для отрицательных индексов.
#Негафибоначчи
#in
#8
#out
#-21 13 -8 5 -3 2 -1 1 0 1 1 2 3 5 8 13 21
#in
#5
#out
#5 -3 2 -1 1 0 1 1 2 3 5

from audioop import reverse


num = int(input('Введите число '))

def fibo_minus(num):
    f1 = 0
    f2 = 1
    fibo_list1 = [f1,f2]
    while num+1 > 2:
        f1, f2 = f2, f1-f2
        fibo_list1.append(f2) 
        num -= 1
    fibo_list1.remove(0)
    return list(reversed(fibo_list1))

def fibo(num):
    f1 = 0
    f2 = 1
    fibo_list1 = [f1,f2]
    while num+1 > 2:
        f1, f2 = f2, f1+f2
        fibo_list1.append(f2) 
        num -= 1
    return fibo_list1

resutl = fibo_minus(num) + fibo(num)
print(resutl)