from random import randint
from statistics import median

list = []
total = 0

for i in range(15):
    num = randint(1,100)
    list.append(num)

sorted = sorted(list)

for i in sorted:
    total += i

print(f'mean: {total/15:.2f}')
print(f'median: {median(sorted)}')
