def main():
    
    list1 = [1,2,4,5,6,7,8]
    list2 = [1,2,3,4,6,7,8,9]
    print(f'{missing_number(list1,8):.0f}')
    print(f'{missing_number(list2,9):.0f}')
    
    
def missing_number(list, n):
    
    total_sum = n * (n + 1) / 2 
    missing = total_sum - sum(list)
    return missing

    
        
if __name__ == '__main__':
    main()
