def  safe_divide (numerator, denominator): 
        
        if not isinstance (numerator,float) or not isinstance(denominator,float):
             raise TimeoutError("Error: Please enter numeric values only.")
        
        if denominator==0:
            raise ZeroDivisionError("Error: Cannot divide by zero.")
        return numerator/numerator


try:
    print(safe_divide(6,2))
except Exception as e:
     print(e)

    
try:
     
     print(safe_divide(6,0))

except ZeroDivisionError as e:
    print(e)

try:
    

    print(safe_divide("ten", 5))


except TypeError as e:
     print(e)






     
      

    


      
    
    
    


    

