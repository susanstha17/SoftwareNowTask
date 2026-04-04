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
            if char <= 'm':
                # If the letter is in the first half (a-m), shift forward
                shift = shift1 * shift2
            else:
                # If the letter is in the second half (n-z), shift backward
                shift = -(shift1 + shift2)
            # Apply the shift to the character and add it to the encrypted data
            encrypted_data += chr((ord(char) - 97 + shift) % 26 + 97)
        elif char.isupper():
            # Apply the second shift value based on the position of the letter in the alphabet
            '''
            For uppercase letters:
                - If the letter is in the first half (A-M): shift backward by shift1 positions
                - If the letter is in the second half (N-Z): shift forward by shift2² positions (shift2 squared)
            '''
            if char <= 'M':
                # If the letter is in the first half (A-M), shift backward
                shift = -shift1
            else:
                # If the letter is in the second half (N-Z), shift forward by shift2² positions
                shift = shift2 ** 2
            # Apply the shift to the character and add it to the encrypted data
            encrypted_data += chr((ord(char) - 65 + shift) % 26 + 65)
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
            '''
            For lowercase letters:
                - If the letter is in the first half of the alphabet (a-m): shift backward by shift1 * shift2 positions
                - If the letter is in the second half (n-z): shift forward by shift1 + shift2 positions
            '''
            if char <= 'm':
                # If the letter is in the first half (a-m), shift backward
                shift = -(shift1 * shift2)
            else:
                # If the letter is in the second half (n-z), shift forward
                shift = shift1 + shift2
            # Apply the shift to the character and add it to the decrypted data
            decrypted_data += chr((ord(char) - 97 + shift) % 26 + 97)
        elif char.isupper():
            # Apply the second shift value based on the position of the letter in the alphabet
            '''
            For uppercase letters:
                - If the letter is in the first half (A-M): shift forward by shift1 positions
                - If the letter is in the second half (N-Z): shift backward by shift2² positions (shift2 squared)
            '''
            if char <= 'M':
                # If the letter is in the first half (A-M), shift forward
                shift = shift1
            else:
                # If the letter is in the second half (N-Z), shift backward by shift2² positions
                shift = -(shift2 ** 2)
            # Apply the shift to the character and add it to the decrypted data
            decrypted_data += chr((ord(char) - 65 + shift) % 26 + 65)
        else:
            # If the character is not a letter, leave it unchanged
            decrypted_data += char
    print(f'Decryption of {encrypted_text_file} has completed.')
    return decrypted_data


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

# call the main function
if __name__ == "__main__":
    main()