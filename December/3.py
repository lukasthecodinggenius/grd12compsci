import re

def main():
    
    password = input('Enter Password: ')
    print(validate(password))
    
    
def validate(password):
    
    if len(password) >= 8 and re.search('[A-Z]+', password) and re.search('[0-9]+', password): #use regular expressions to check for more than one instance of capital letters and digits
        return True
    else:
        return False
    
    
        
    
        

main()
