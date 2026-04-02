def main():
    print("Hello, World!")
    with open("/InputOutput/raw_text.txt", "r") as file:
        data = file.read()
        print(data)
if __name__ == "__main__":
    main()