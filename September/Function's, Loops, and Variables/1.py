def main():
    #take input
    number = input('Input Number: ')
    type = evenorodd(number)

    #print based on result
    if type == True:
        print('even')
    else:
        print('odd')

def evenorodd(num):
    #if the remainer when divided by 2 is 0, then the number is even
    if int(num) % 2 == 0:
        return True
    else:
        return False

main()
