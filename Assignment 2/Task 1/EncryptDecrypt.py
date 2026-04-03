import os
print(os.getcwd())

# encryption function
def encrypt(raw_text, shift1, shift2):
    # check if the file exists
    if not os.path.exists(raw_text):
        print(f"File {raw_text} does not exist.")
        return
    # Read the contents of the file "raw_text.txt"
    with open(raw_text, "r") as file:
        data = file.read()
        print(data)
    print(f'Encryption of {raw_text} has started with shift values {shift1} and {shift2}')

#main function
def main():
    print("Hello, World!")
    raw_text = "Assignment 2/Task 1/InputOutput/raw_text.txt"
    encrypted_text = "Assignment 2/Task 1/InputOutput/encrypted_text.txt"
    decrypted_text = "Assignment 2/Task 1/InputOutput/decrypted_text.txt"
    
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
    # Encrypt the data using the shift values
    encrypted_data = encrypt(raw_text, shift1, shift2)
    # with open(encrypted_text, "w") as file:
    #     file.write(encrypted_data)
    # print("Data encrypted successfully.")
    # # Decrypt the data
    # decrypted_data = decrypt(encrypted_data, shift1, shift2)
    # with open(decrypted_text, "w") as file:
    #     file.write(decrypted_data)
    # print("Data decrypted successfully.")

# call the main function
if __name__ == "__main__":
    main()