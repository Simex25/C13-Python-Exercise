if __name__ == '__main__':
    input("What is your problem? \n")

    reply = input("Have you had this problem before(yes / no)?\n ").lower()

    if reply == 'yes':
        print("Well, you have it again.")

    elif reply == 'no':
        print("Well, you have it now.")
