def main():
    
    string = input('Enter String: ')
    vowelcount = vowels(string)
    print(f'There are {vowelcount} Vowels in the string')
    

def vowels(string):
    
    count = 0
  
    for i in string:
        if i.lower() in ['a', 'e', 'i', 'o', 'u']:
            count += 1
            
    return count
        

main()
