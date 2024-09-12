def palindrome(w):
    return w == w[::-1]

check = input('enter word: ')

if palindrome(check) == True:
    print('yes')
else:
    print('no')
