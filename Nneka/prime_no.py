if __name__ == '__main__':
    prime = int(input("Enter a number:"))
    i = 1
    no = 0
    while i <= prime:
        rem = prime % i
        if rem == 0:
            no = no + 1
        i = i + 1
    if no > 2:
        print("It is not a prime number")
    else:
        print("It is a prime number")
