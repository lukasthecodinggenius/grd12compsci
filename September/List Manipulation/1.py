def main():

    list = [1, 2, 3, 4, 5]
    doubled_list = double_values(list)
    print(doubled_list)


def double_values(list):

    newlist = []

    for i in list:
        newlist.append(i*2)
    return newlist




main()
