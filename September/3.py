def main():
    
    
    celcius = float(input('Input Temperature in Celcius: '))
    fahrenheit, kelvin = (celcius * (9/5) + 32), (celcius + 273.15)
    print(f'{fahrenheit}F or {kelvin}K')
    
main()
