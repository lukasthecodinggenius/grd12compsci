def main():
    
    string = input('Input: ')
    print(frequent_character(string))
    
def frequent_character(string):
    
    dict = {}
    
    for letter in string:
        if letter in dict:
            dict[letter] += 1
        else:
            dict[letter] = 1
    
    max = 0
    
    for letter in string:
        if dict[letter] > max:
            max = dict[letter]
            frequent = letter
    return frequent
    
    
main()
