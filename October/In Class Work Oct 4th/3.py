def main():
    
    string = input('Input: ').lower().strip().replace(" ", "")
    string = ''.join(char for char in string if char.isalnum())
    print(string)
    print(palindrome(string))
    
def palindrome(string):
    
    if string == string[::-1]:
        return True
    else:
        return False
    
main()
