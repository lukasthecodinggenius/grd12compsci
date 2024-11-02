def main():
    
    list1 = [34,25,65,23,5,3,898,535,78974,235,7]
    list2 = [1,2,3,3,4,5,6,7]
    list3 = [1,2,3,4,5,6,7]
    list4 = [1,3,4,5,6,7,7,7,7,5,5,5,23,4,234,234]
    print(doubles(list1))
    print(doubles(list2))
    print(doubles(list3))
    print(doubles(list4))
    
    
    
def doubles(list):
    for i in list:
        if list.count(i) > 1:
            return True
    return False
        
    
        
if __name__ == '__main__':
    main()
