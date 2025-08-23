
def factorial(n):
    if n < 0:
        return "Error: Factorial is not defined for negative numbers."
    elif n == 0:
        return 1
    else:
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result

def main():
    
    try:
        num = int(input("Enter a non-negative integer: "))
        fact_result = factorial(num)
        print(f"The factorial of {num} is: {fact_result}")

    except ValueError:
        print("\nError: Invalid input. Please enter a whole number.")

if __name__ == "__main__":
    main()