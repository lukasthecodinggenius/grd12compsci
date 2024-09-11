import random

lst = []
total = 0

for i in range(10):
    number = random.randint(0,1)
    lst.append(number)

for num in lst:
    total += num

print(total/10)
