file_name = 'sample.txt'

try:
    with open(file_name, 'r') as file:
        for line in file:
            print(line)
        print("--- End of File ---")

except FileNotFoundError:
    print(f"Error: The file named '{file_name}' could not be found.")