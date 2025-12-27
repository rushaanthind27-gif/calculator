def calculator():
    print("Simple Calculator")
    print("Operations: +, -, *, /")
    print("Type 'quit' to exit")
    
    while True:
        try:
            # Get user input
            num1 = float(input("Enter first number: "))
            op = input("Enter operation (+, -, *, /): ")
            if op.lower() == 'quit':
                break
            num2 = float(input("Enter second number: "))
            
            # Perform calculation
            if op == '+':
                result = num1 + num2
            elif op == '-':
                result = num1 - num2
            elif op == '*':
                result = num1 * num2
            elif op == '/':
                if num2 == 0:
                    print("Error: Division by zero")
                    continue
                result = num1 / num2
            else:
                print("Invalid operation")
                continue
            
            print(f"Result: {result}")
        except ValueError:
            print("Invalid input. Please enter numbers.")

# Run the calculator
calculator()
