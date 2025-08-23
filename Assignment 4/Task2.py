file_name = 'output.txt'

try:
    user_content = input("Please enter a sentence to write to the file: ")

    with open(file_name, 'w') as file:
        file.write(user_content + '\n')

    user_content1 = input("Please enter a additional sentence to append to the file: ")

    with open(file_name, 'a') as file:
        file.write("" + user_content1 + '\n')

    print(f"\n--- Final Content of {file_name} ---")
    with open(file_name, 'r') as file:
        print(file.read().strip())

except IOError as e:
    print(f"An error occurred during file operations: {e}")
