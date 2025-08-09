def perform_operation(num1,num2,operation):
    if operation == "add":
        ans = num1 + num2
        
    elif operation == "subtract":
        ans = num1 - num2
        
    elif operation == "multiply":
        ans = num1 * num2
        
    elif operation == "divide":
        if num2 <= 0:
            ans = "the second number must be greeter than zero"
        else:
            ans = num1 / num2
    else:
        ans = "Invalid input"

    return ans