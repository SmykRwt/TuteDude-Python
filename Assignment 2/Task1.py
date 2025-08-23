def main():

    try:
        number = int(input("Enter an integer: "))

        if number % 2 == 0:
            print(f"The number {number} is Even.")
        else:
            print(f"The number {number} is Odd.")

    except ValueError:
        print("\nError: Invalid input.")

if __name__ == "__main__":
    main()