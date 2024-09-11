list = [4, 5 , 3.5, 12.5]
max = 0


for i in list:
    if i > max:
        max = i

print(max)

min = max

for i in list:
    if i < min:
        min = i

print(min)
