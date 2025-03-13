def calculate():
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    print("\nAvailable operations: +, -, *, /")
    operation = input("Enter the operation you want to perform: ")
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == '/':
        if num2 == 0:
            print("Error: Division by zero is not allowed!")
            return
        result = num1 / num2
    else:
        print("Invalid operation entered!")
        return
        print("The result is: ", result)
    calculate()