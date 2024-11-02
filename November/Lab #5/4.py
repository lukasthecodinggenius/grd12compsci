def main():
    list1 = sorted([1,56,8,123,54123,2])
    list2 = sorted([2,3,4,5,123561234])
    print(mergesorted(list1,list2))


def mergesorted(list1, list2):
    mergedlist = []
    i = 0
    j = 0

    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            mergedlist.append(list1[i])
            i += 1
        else:
            mergedlist.append(list2[j])
            j += 1

    while i < len(list1):
        mergedlist.append(list1[i])
        i += 1

    while j < len(list2):
        mergedlist.append(list2[j])
        j += 1

    return mergedlist

if __name__ == '__main__':
    main()
