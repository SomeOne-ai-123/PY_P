def divide_numbers(num1, num2):
    try:
        # Try to perform the division
        result = num1 / num2
    except ZeroDivisionError as e:
        # Handle division by zero error
        print("Error: Cannot divide by zero.")
        print(f"Exception details: {e}")
    except TypeError as e:
        # Handle wrong data type error
        print("Error: Invalid input type. Please enter numbers.")
        print(f"Exception details: {e}")
    except Exception as e:
        # Handle any other exceptions
        print("An unexpected error occurred.")
        print(f"Exception details: {e}")
    else:
        # This block executes if no exceptions were raised
        print(f"The result of the division is: {result}")
    finally:
        # This block always executes
        print("Execution of the divide_numbers function is complete.")

# program ends here______________________________________________________________________
# Test the function with different inputs

# Case 1: Valid division
divide_numbers(10, 2)

# Case 2: Division by zero
divide_numbers(10, 0)

# Case 3: Invalid input type
divide_numbers(10, 'a')

# Case 4: Another valid division
divide_numbers(15, 3)
