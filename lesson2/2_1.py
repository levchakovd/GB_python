num = float(input('Введите вещественное число '))
count = 0
while (num > 0):
    count = count + num % 10
    num = num // 10
print(count)
