list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

evenlist = []
oddlist = []

for number in list:
    if number%2 == 0:
        evenlist.append(number)
    else:
        oddlist.append(number)

print(evenlist, oddlist)
