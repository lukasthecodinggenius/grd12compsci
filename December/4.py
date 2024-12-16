

def main():
    
    string = input('Enter String: ')
    print(palindrome(string))
    
    
def palindrome(string):
    
    return string == string[::-1]
        

main()
