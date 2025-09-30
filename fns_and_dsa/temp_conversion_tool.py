FAHRENHEIT_TO_CELCIUS_FACTOR = 5/9
CELSIUS_TO_FACTOR = 9/5

def  convert_to_celsius(fahrenheit):
    Temperature = float (input("Enter the temperature to convert: "))
    Temperature_conversion = (input("Is this temperature in Celsius or Fahrenheit? (C/F): "))
    f_temp = (fahrenheit-32) *FAHRENHEIT_TO_CELCIUS_FACTOR
    print (f_temp)
convert_to_celsius(12)


    



def convert_to_farenheit(celsius):
    Temperature = float(input("Enter the temperature to convert: "))
    Temperature_conversion = input("Is this temperature in Celsius or Fahrenheit? (C/F): ")
    c_temperature =  celsius*CELSIUS_TO_FACTOR +32
    print(c_temperature)
convert_to_farenheit(13)
