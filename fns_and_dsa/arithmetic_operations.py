

def perform_operation (num1,num2,operation):

    if operation == "add":
        result = num1 + num2
        return result
    elif operation == "subtract":
        result1 = num1 - num2
        return result1
    elif operation == "multiply":
        result2 = num1 * num2
        return result2
    elif operation == "divide":
        if num2 == 0:
            return "Division by zero is not allowed"
        result3 = num1/num2
        return result3

    else:
        return "Unknown operation"
    
    
    
    





















def main():
    print("Arithmetic Operations")
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operation = input("Enter the operation (add, subtract, multiply, divide): ").strip().lower()

    result = perform_operation(num1, num2, operation)
    print(f"Result: {result}")

if __name__ == "__main__":
    main()