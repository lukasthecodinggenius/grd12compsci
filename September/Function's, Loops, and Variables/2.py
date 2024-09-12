def main():
    #take input
    num = int(input('input number: '))
    final = factorial(int(num))
    print(final)

def factorial(num):
    total = 1
    for i in range(1, num+1): #for loop will repeat num+1 amount of times
        total *= i #total = total * i
    return total #return the factorial of the number

main() #call main
