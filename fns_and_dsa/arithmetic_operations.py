def perform_operation(num1, num2, operation):
    if operation == "add":
        sum = num1 + num2
        return sum
    elif operation == "subtract":
        sub = num1 - num2
        return sub
    elif operation == "multiply":
        mult = num1 * num2
        return mult
    elif operation == "divide":
        if num2 <= 0:
            print("the second number must be greeter than zero")
        else:
            div = num1 / num2
            return div
    