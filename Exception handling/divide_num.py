def divide_numbers():
    try:
        numerator = float(input("Enter numerator: "))
        denominator = float(input("Enter denominator: "))
        result = numerator / denominator
        
    except ZeroDivisionError:
        print("Error: You cannot divide a number by zero.")
        
    except ValueError:
        print("Error: Please enter valid numbers only.")
        
    else:
        print(f"Success! The result is: {result}")
        
    finally:
        print("Division operation completed.")

divide_numbers()
