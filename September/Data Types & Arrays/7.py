list = [1,2,3,4,5]
newlist = []

for i in list:
    newlist.append(i*2)

del newlist[-1]
del newlist[-1]

for i in range(2):
    num = input('What do you want to append to the list?')
    newlist.append(num)


print(newlist)
