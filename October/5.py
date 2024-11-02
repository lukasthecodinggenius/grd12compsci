def main():
    list1 = [2,4,6,8,10,12,128301823,453]
    list2 = [1,3,5,7,9,10,12,1238,453]
    intersections = intersection(list1,list2)
    for i in intersections:
        print(i)


def intersection(list1,list2):
    
    intersections = []
    for num in list1:
        if num in list2 and num not in intersections:
            intersections.append(num)
    return intersections

if __name__ == '__main__':
    main()
