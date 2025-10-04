def divide(x,y):

        if y==0:
            raise ZeroDivisionError("Error: Cannot divide by zero.")
        return x/y
try:
    print(divide(6,2))
    print(divide(6,0))
    print(6,c)

except ZeroDivisionError as e:
     print(e)

except TypeError:
     raise ValueError ("Error: Please enter numeric values only.")





     
      

    


      
    
    
    


    

