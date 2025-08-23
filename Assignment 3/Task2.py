import math
def main():
    try:
        number = float(input("Enter a number: "))
        sqrt_result = "N/A"
        log_result = "N/A"
        if number >= 0:
            sqrt_result = math.sqrt(number)
            log_result = math.log(number)
        sine_result = math.sin(number)

        print(f"The number you entered is: {number}")
        print(f"Square Root:      {sqrt_result}")
        print(f"Logarithm   : {log_result}")
        print(f"Sine:  {sine_result}")

    except ValueError:
        print("\nError: Invalid input. Please enter a valid number.")
        
if __name__ == "__main__":
    main()
