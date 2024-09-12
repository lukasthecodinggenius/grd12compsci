def main():
    num = int(input('input number: '))
    final = factorial(int(num))
    print(final)

def factorial(num):
    total = 1
    for i in range(1, num+1):
        total *= i
    return total

main()
