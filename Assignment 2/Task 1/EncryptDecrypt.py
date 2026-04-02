#main function
def main():
    print("Hello, World!")
    # Read the contents of the file "raw_text.txt"
    with open("/InputOutput/raw_text.txt", "r") as file:
        data = file.read()
        print(data)

# call the main function
if __name__ == "__main__":
    main()