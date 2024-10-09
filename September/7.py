def main():
    
   
    word = balanced(input('Input: '))
    print(word)
    
    
def balanced(string):
   
    words = string.split()
    max = words[0]
   
    for i in words:
        if len(i) > len(max):
           max = i
    return max
    
    
main()
