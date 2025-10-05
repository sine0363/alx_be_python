def safe_divide(numerator, denominator):
    try:
    
        numerator = float(numerator)
        denominator = float(denominator)
    except ValueError:
        raise TypeError("Error: Please enter numeric values only.")
    
    if denominator == 0:
        raise ZeroDivisionError("Error: Cannot divide by zero.")
    
    return numerator / denominator


# Test cases
try:
    print(f"The result of the division is {safe_divide(6, 2)}")
  
    
  
except Exception as e:
    print(e)

try:
    print(safe_divide(6, 0))
except ZeroDivisionError as e:
    print(e)

try:
    print(safe_divide("ten", 5))
except TypeError as e:
    print(e)


 
