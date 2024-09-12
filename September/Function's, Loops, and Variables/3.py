def palindrome(w):
    #return True or False based on the reversed value of the string
    return w == w[::-1]

check = input('enter word: ') #take input

if palindrome(check) == True: #output based on the result of calling palindrome
    print('yes')
else:
    print('no')
