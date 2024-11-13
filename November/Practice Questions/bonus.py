d = {}

# to exit program and print out the dict, press control-d on keyboard
while True:
    try:
        count = 1
        item = input().upper()
        if item in d:
            d[item] = count + 1
        else:
            d[item] = count
    except EOFError:
        if len(d) == 0:
            exit()
        d = sorted(d.items())
        for i, j in d:
            print(j, i, sep=" ")
        exit()

