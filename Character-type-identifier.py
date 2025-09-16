# charcature type cheaker

def check_char(char):
    if len(char) == 1:
        if char.isupper():
            print("Entered char is in uppercase")
        elif char.islower():
            print("Entered char is in lowercase")
        elif char.isdigit():
            print("Entered char is a number")
        else:
            print("Entered char is a special symbol")
    else:
        print("Invalid input! Please enter only one character.")

symbol = input("Enter your symbol: ")

check_char(symbol)