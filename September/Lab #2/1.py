def main():
    
    try:
        num1 = input('Enter First Number: ')
        num2 = input('Enter Second Number: ')
    except ValueError:
        print('Make sure to enter a number')
    
    num1, num2 = num2, num1
    
    print(f'Original numbers: {num2, num1}, Swapped numbers: {num1, num2}')

main()
