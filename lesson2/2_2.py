n = int(input('введите число '))
sum = 1

for i in range(n):
    sum *= i + 1
    print(sum, end =", ")