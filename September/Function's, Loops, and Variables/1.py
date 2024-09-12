def main():
    number = input('Input Number: ')
    type = evenorodd(number)

    if type == True:
        print('even')
    else:
        print('odd')

def evenorodd(num):
    if int(num) % 2 == 0:
        return True
    else:
        return False

main()
