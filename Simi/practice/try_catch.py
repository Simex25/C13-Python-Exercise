
try:
    number = int(input("Enter an integer"))
except ValueError:
    print("Try again")
    number = int(input("Enter an integer"))
    while number != " ":
        number = int(input("Enter an integer"))
        number = number + 1
