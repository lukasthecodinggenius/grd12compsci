def main():
    
    
    print(remove_vowels(input('Input: ')))   
 
    
def remove_vowels(word):
    
    vowels = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']
    
    for letter in word:
        if letter in vowels:
            word = word.replace(letter, '')
    return word
    
    
main()
