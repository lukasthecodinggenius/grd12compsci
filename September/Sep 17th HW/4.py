from random import randint
def main():

    list = []
    for i in range(20):
        num = randint(1,100)
        list.append(num)

    primelist = filter_primes(list)
    print(f'list of numbers: {list}')
    print(f'list of primes: {primelist}')




def is_prime(num):

    if num == 0 or num == 1:
        return False
    elif num > 1:
        for i in range(2,num):
            if (num % i) == 0:
                return False
                break
        return True




def filter_primes(list):

    primelist = []
    for i in list:
        if is_prime(i) == True:
            primelist.append(i)
    return primelist




main()
