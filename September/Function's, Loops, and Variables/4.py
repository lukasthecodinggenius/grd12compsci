def main():
    for i in range(51): #this for loop will repeat 51 times
        if i % 3 == 0 and i % 5 == 0: #first, check if the number is a factor of 3 and 5
            print('FizzBuzz')
        elif i % 3 == 0: #then check if its a factor of 3 
            print('Fizz')
        elif i % 5 == 0: #then check if its a factor of 5
            print('Buzz')
        else:
            print(i) #if it doesn't meet any of the requirements, just print I

main()
