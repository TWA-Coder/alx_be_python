def safe_divide(numerator, denominator):

    try:
        fl_numerator = float(numerator)
        fl_denominator = float(denominator)
        divide = fl_numerator/fl_denominator

        return divide
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")

    except ValueError:
        print("Error: Please enter numeric values only.")
    


        
       
            