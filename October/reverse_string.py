def main():
    string = str(input('Input: '))
    print(reverse(string))
    
def reverse(s):
    return s[::-1]

if __name__ == '__main__':
    main()
