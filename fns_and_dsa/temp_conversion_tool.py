FAHRENHEIT_TO_CELSIUS_FACTOR = 9/5
CELSIUS_TO_FAHRENHEIT_FACTOR  = 5/9

def convert_to_celsius(fahrenheit):
    temp_celsius = float(CELSIUS_TO_FAHRENHEIT_FACTOR * (fahrenheit - 32))

    print(f"{fahrenheit}°F is {temp_celsius}°C")

def convert_to_fahrenheit(celsius):
    temp_fahrenheit = float( FAHRENHEIT_TO_CELSIUS_FACTOR * (celsius + 32))

    print(f"{celsius}°C is {temp_fahrenheit}°F")    

def main():
    temp = float(input("Enter the temperature to convert: "))

    type = str(input("Is this temperature in Celsius or Fahrenheit? (C/F):")).capitalize()
    if type == 'C':
        convert_to_fahrenheit(temp)
    elif type =='F':
        convert_to_celsius(temp)
    else:
        print("Invalid input")

if __name__ =="__main__":
    main()
