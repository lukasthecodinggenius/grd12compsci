def main():
    
    print(area(int(input('radius: '))))
    
def area(r):
    
    area = 3.14159 * (r * r)
    return area
    
if __name__ == '__main__':
    main()
