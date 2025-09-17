size = int(input("Enter the size of the pattern:"))
rows =0 


while rows < size:
    col = 0
    while col < size:
        print("*", end="")  
        col += 1
    print()  
    rows += 1
