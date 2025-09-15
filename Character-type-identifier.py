# charcature type cheaker
char = input("Enter your symbol")

if len(char) == 1:
    if 'A' <= char <= 'Z':
        print("Entered char is in upppercase")
    elif 'a' <= char <= 'z':
        print("Entered char is in lower case")
    elif '1' <= char <= '9':
        print("Entered char is in number formet")

else:
    print("invalid char")  
