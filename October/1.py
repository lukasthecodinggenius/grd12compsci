def main():
    
    list1 = [1,5,123,5,5,3,123,5,7,8,56,3,124,25,8,86,3,245,2]
    list2 = [2,6,4,7,9,989,78676,43,4678,9765,32,245,77]
    list3 = [34,25,65,23,5,3,898,535,78974,235,7]
    print(secondlargest(list1))
    print(secondlargest(list2))
    print(secondlargest(list3))
    
    
def secondlargest(list):
    
    list = sorted(list)
    return list[-2]
    
    
if __name__ == '__main__':
    main()
