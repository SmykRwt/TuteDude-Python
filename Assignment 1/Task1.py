def main():
    try:

        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        
        addition_result = num1 + num2
        subtraction_result = num1 - num2
        multiplication_result = num1 * num2
        if num2 != 0:
            division_result = num1 / num2
        else:
            division_result = "Error: Cannot divide by zero."

        print(f"Addition:       {num1} + {num2} = {addition_result}")
        print(f"Subtraction:    {num1} - {num2} = {subtraction_result}")
        print(f"Multiplication: {num1} * {num2} = {multiplication_result}")

        if num2 != 0:
            print(f"Division:   {num1} / {num2} = {division_result}")
        else:
            print(f"Division:       {division_result}")
    except ValueError:
        print("\nError: Invalid input. Please enter valid numbers.")

if __name__ == "__main__":
    main()