def main():
    
   
    print(balanced(input('Input: ')))
    
    
def balanced(string):
    
    left = string.count('(')
    right = string.count(')')
    
    if left == right:
        return True
    else:
        return False
    
main()
