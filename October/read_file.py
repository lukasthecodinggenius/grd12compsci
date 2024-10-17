def main():
    
    path = input('input txt file: ')
    print(read_file(path))
    
    
def read_file(path):
    
    with open(path, 'r') as file:
        info = file.read()
    return info

if __name__ == '__name__':
    main()
    
