

def main():
    
    string = input('Enter String: ')
    print(palindrome(string))
    
    
def palindrome(string):
    
    return string == string[::-1] #check if the string is the same when reversed, return True if it is, False if it isnt
        

main()
