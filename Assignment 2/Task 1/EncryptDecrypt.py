import os
print(os.getcwd())
#main function
def main():
    print("Hello, World!")
    file_path = "Assignment 2/Task 1/InputOutput/raw_text.txt"
    # check if the file exists
    if not os.path.exists(file_path):
        print(f"File {file_path} does not exist.")
        return
    # Read the contents of the file "raw_text.txt"
    with open(file_path, "r") as file:
        data = file.read()
        print(data)
    # ask user for two shift values
    shift1 = int(input("Enter first shift value (1-25): "))
    # validate first shift value
    if shift1 < 1 or shift1 > 25:
        print("Invalid shift value. Please enter a value between 1 and 25.")
        return
    shift2 = int(input("Enter second shift value (1-25): "))
    # validate second shift value
    if shift2 < 1 or shift2 > 25:
        print("Invalid shift value. Please enter a value between 1 and 25.")
        return

# call the main function
if __name__ == "__main__":
    main()