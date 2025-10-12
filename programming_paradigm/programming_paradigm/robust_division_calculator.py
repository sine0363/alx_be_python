def safe_divide(numerator, denominator):
    try:
        numerator = float(numerator)
        denominator = float(denominator)
    except ValueError:
        raise TypeError("Error: Please enter numeric values only.")
    
    if denominator == 0:
        raise ZeroDivisionError("Error: Cannot divide by zero.")
    
    return numerator / denominator



print(f"The result of the division is {safe_divide(12, 2)}")