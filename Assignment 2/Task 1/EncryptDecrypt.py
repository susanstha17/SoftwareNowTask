import os

# encryption function
def encrypt_textFile(raw_text_file, shift1, shift2):
    # check if the file exists
    if not os.path.exists(raw_text_file):
        print(f"File {raw_text_file} does not exist.")
        return ""
    # Read the contents of the file "raw_text.txt"
    with open(raw_text_file, "r") as file:
        raw_data = file.read()
        print(raw_data)
    print(f'Encryption of {raw_text_file} has started with shift values {shift1} and {shift2}')
    # Initialize an empty string to store the encrypted data
    encrypted_data = ""
    # Iterate through each character in the raw data and apply the appropriate shift based on whether it's uppercase or lowercase
    for char in raw_data:
        # Check if the character is lowercase
        if char.islower():
            # Apply the first shift value based on the position of the letter in the alphabet
            '''
            For lowercase letters:
                - If the letter is in the first half of the alphabet (a-m): shift forward by shift1 * shift2 positions
                - If the letter is in the second half (n-z): shift backward by shift1 + shift2 positions
            '''
            if 'a' <= char <= 'm':
                # If the letter is in the first half (a-m), shift forward
                shift = shift1 * shift2
                encrypted_data += chr((ord(char) - ord('a') + shift) % 13 + ord('a')) # Apply the shift to the character and add it to the encrypted data
            else:
                # If the letter is in the second half (n-z), shift backward
                shift = -(shift1 + shift2)
                encrypted_data += chr((ord(char) - ord('n') + shift) % 13 + ord('n')) # Apply the shift to the character and add it to the encrypted data
            # Apply the shift to the character and add it to the encrypted data
            # encrypted_data += chr((ord(char) - 97 + shift) % 26 + 97) -- This line is commented out because the shift is applied differently based on the position of the letter in the alphabet (a-m or n-z)
        elif char.isupper():
            # Apply the second shift value based on the position of the letter in the alphabet
            '''
            For uppercase letters:
                - If the letter is in the first half (A-M): shift backward by shift1 positions
                - If the letter is in the second half (N-Z): shift forward by shift2² positions (shift2 squared)
            '''
            if 'A' <= char <= 'M':
                # If the letter is in the first half (A-M), shift backward
                shift = -shift1
                encrypted_data += chr((ord(char) - ord('A') + shift) % 13 + ord('A')) # Apply the shift to the character and add it to the encrypted data
            else:
                # If the letter is in the second half (N-Z), shift forward by shift2² positions
                shift = shift2 ** 2
                encrypted_data += chr((ord(char) - ord('N') + shift) % 13 + ord('N')) # Apply the shift to the character and add it to the encrypted data
            # Apply the shift to the character and add it to the encrypted data
            # encrypted_data += chr((ord(char) - 65 + shift) % 26 + 65) -- This line is commented out because the shift is applied differently based on the position of the letter in the alphabet (A-M or N-Z)
        else:
            # If the character is not a letter, leave it unchanged
            encrypted_data += char
    print(f'Encryption of {raw_text_file} has completed.')
    return encrypted_data

# decryption function
def decrypt_textFile(encrypted_text_file, shift1, shift2):
    # check if the file exists
    if not os.path.exists(encrypted_text_file):
        print(f"File {encrypted_text_file} does not exist.")
        return ""
    # Read the contents of the file "encrypted_text.txt"
    with open(encrypted_text_file, "r") as file:
        encrypted_data = file.read()
        print(encrypted_data)
    print(f'Decryption of {encrypted_text_file} has started with shift values {shift1} and {shift2}')
    # Initialize an empty string to store the decrypted data
    decrypted_data = ""
    # Iterate through each character in the encrypted data and apply the appropriate shift based on whether it's uppercase or lowercase
    for char in encrypted_data:
        # Check if the character is lowercase
        if char.islower():
            # Apply the first shift value based on the position of the letter in the alphabet
            if 'a' <= char <= 'm':
                # If the letter is in the first half (a-m), shift backward
                shift = -(shift1 * shift2)
                decrypted_data += chr((ord(char) - ord('a') + shift) % 13 + ord('a')) # Apply the shift to the character and add it to the decrypted data
            else:
                # If the letter is in the second half (n-z), shift forward
                shift = shift1 + shift2
                decrypted_data += chr((ord(char) - ord('n') + shift) % 13 + ord('n')) # Apply the shift to the character and add it to the decrypted data
            # Apply the shift to the character and add it to the decrypted data
            #decrypted_data += chr((ord(char) - 97 + shift) % 26 + 97) -- This line is commented out because the shift is applied differently based on the position of the letter in the alphabet (a-m or n-z)
        elif char.isupper():
            # Apply the second shift value based on the position of the letter in the alphabet
            if 'A' <= char <= 'M':
                # If the letter is in the first half (A-M), shift forward
                shift = shift1
                decrypted_data += chr((ord(char) - ord('A') + shift) % 13 + ord('A')) # Apply the shift to the character and add it to the decrypted data
            else:
                # If the letter is in the second half (N-Z), shift backward by shift2² positions
                shift = -(shift2 ** 2)
                decrypted_data += chr((ord(char) - ord('N') + shift) % 13 + ord('N')) # Apply the shift to the character and add it to the decrypted data
            # Apply the shift to the character and add it to the decrypted data
            #decrypted_data += chr((ord(char) - 65 + shift) % 26 + 65) -- This line is commented out because the shift is applied differently based on the position of the letter in the alphabet (A-M or N-Z)
        else:
            # If the character is not a letter, leave it unchanged
            decrypted_data += char
    print(f'Decryption of {encrypted_text_file} has completed.')
    return decrypted_data

# Function to verify the integrity of the decrypted data
def verify_content(original_file, decrypted_file):
    # Check if the original and decrypted files match
    with open(original_file, "r") as file1, open(decrypted_file, "r") as file2:
        return file1.read() == file2.read()

# Function to get a valid shift value from the user
def get_shift_value(prompt):
    # Loop until a valid shift value is entered
    while True:
        try:
            # Get the shift value from the user and convert it to an integer
            shift = int(input(prompt))
            if 1 <= shift <= 25:
                return shift
            else:
                # If the shift value is not between 1 and 25, print an error message and prompt the user again
                print("Invalid shift value. Please enter a value between 1 and 25.")
        except ValueError:
            # If the input is not a valid integer, print an error message and prompt the user again
            print("Invalid input. Please enter a numeric value between 1 and 25.")

#main function
def main():
    # Define file paths for raw text, encrypted text, and decrypted text
    raw_text = "Assignment 2/Task 1/InputOutput/raw_text.txt"
    encrypted_text = "Assignment 2/Task 1/InputOutput/encrypted_text.txt"
    decrypted_text = "Assignment 2/Task 1/InputOutput/decrypted_text.txt"
    
    # ask user for two shift values between 1 and 25, and validate the input
    shift1 = get_shift_value("Enter first shift value (1-25): ")
    shift2 = get_shift_value("Enter second shift value (1-25): ")

    # call the encrypt_text function to encrypt the data using the shift values
    encrypted_data = encrypt_textFile(raw_text, shift1, shift2)
    with open(encrypted_text, "w") as file:
        file.write(encrypted_data)
    print("Data encrypted successfully.")

    # call the decrypt_textFile function to decrypt the data
    decrypted_data = decrypt_textFile(encrypted_text, shift1, shift2)
    with open(decrypted_text, "w") as file:
        file.write(decrypted_data)
    print("Data decrypted successfully.")

    # Verify the integrity of the decrypted data
    if verify_content(raw_text, decrypted_text):
        print("Verification successful! Original and decrypted data match.")
    else:
        print("Verification failed! Original and decrypted data do not match.")

# call the main function
if __name__ == "__main__":
    main()