from unittest import result


num = int(input())
sum_nums = 0
list_nums = []

for i in range(1, num +1):
    result = round((1+1/i)**i)
    list_nums.append(result)
    sum_nums +=result

print(list_nums)
print(sum_nums)