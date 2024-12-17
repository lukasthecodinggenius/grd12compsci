num = int(input("Enter a number: "))
if num > 1:
    prime = True
    for i in range(2, num): #go through all numebrs from 2 to num and check if they are divisible by num
        if num % i == 0:
            prime = False
            break
    if prime:
        print(num, "is a prime number")
    else:
        print(num, "is not a prime number")
else:
    print(num, "is not a prime number")
