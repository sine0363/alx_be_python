
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def  convert_to_celsius(fahrenheit):
    try:
        Temperature =  input("Enter the temperature to convert: ")
        number = float(Temperature)
        Temperature_conversion = (input("Is this temperature in Celsius or Fahrenheit? (C/F): "))
        f_temp = (fahrenheit-32) *FAHRENHEIT_TO_CELSIUS_FACTOR
    except ValueError:
        print("Value entered is not a number")
    print (f_temp)
convert_to_celsius(12)


    



def convert_to_farenheit(celsius):
    try:
        Temperature = float(input("Enter the temperature to convert: "))
        number1= float(Temperature)
        Temperature_conversion = input("Is this temperature in Celsius or Fahrenheit? (C/F): ")
        c_temperature =  celsius*CELSIUS_TO_FAHRENHEIT_FACTOR +32
        print(c_temperature)
    except ValueError:
        print("Value entered is not a number")

        
convert_to_farenheit(13)
