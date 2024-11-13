def main():
    
    print(convert_to_farenheit(float(input('Enter Temperature in Celcius: '))), 'F')
    print(even_or_odd(int(input('Enter Number: '))))
    print(calculator(input('Enter Expression: ')))
    print(multiplication_table(int(input('Enter Number: '))))
    print(grade_calculator(int(input('Enter Grade: '))))
    
def convert_to_farenheit(n):
    
    return (n*9/2) + 32
    
    
def even_or_odd(n):
    
    return 'Even' if n % 2 == 0 else 'Odd'

def calculator(str):
    
    num1, operator, num2 = str.split()
    num1, num2 = int(num1), int(num2)
    if operator == '+':
        return num1+num2
    elif operator == '-':
        return num1-num2
    elif operator == '*':
        return num1*num2
    elif operator == '/':
        return num1/num2
    
def multiplication_table(n):
    
    list = []
    for i in range(10):
        list.append(i * int(n))
        i+=1
    return list

def grade_calculator(grade):
    
    if grade <= 100 and grade >= 90:
        return 'A'
    elif grade <= 89 and grade >= 80:
        return 'B'
    elif grade <= 79 and grade >= 70:
        return 'C'
    elif grade <= 69 and grade >= 60:
        return 'D'
    elif grade < 60:
        return 'F'
    else:
        return 'Invalid Grade'
    
    
    
    
if __name__ == '__main__':
    main()
