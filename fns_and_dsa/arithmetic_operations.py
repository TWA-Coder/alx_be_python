def perform_operation(num1, num2, operation):

    match operation:
        case x if x =="add": 
            ans = num1 + num2
        case x if x =="subtract":
            ans = num1 - num2

        case x if x =="multiply":
            ans = num1 * num2

        case x if x =="divide":
            if num2 <= 0:
                ans = "the second number must be greeter than zero"
            else:
                ans = num1 / num2

        case _:
            ans = "Invalid input" 
        
    return ans