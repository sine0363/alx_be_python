def divide(x,y):

        if y==0:
            raise ZeroDivisionError("Error: Cannot divide by zero.")
        return x/y


try:
    print(divide(6,2))
except Exception as e:
     print(e)

    
try:
     print(divide(6,0))

except ZeroDivisionError as e:
    print(e)

try:
    print(divide("ten", 5))


except TypeError:
    print  ("Error: Please enter numeric values only.")







     
      

    


      
    
    
    


    

