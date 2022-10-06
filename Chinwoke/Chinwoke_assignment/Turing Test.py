if __name__ == '__main__':

    user_input = input("What is your problem?: ")
    user_input2 = input("have you had this problem before yes / no?: ")
    while user_input2 != 'yes' and user_input2 != 'no':
        print("invalid response, pls enter 'yes or no'")
        user_input2 = input("have you had this problem before yes / no?: ")
    if user_input2 == 'yes':
        print("well, you have it again!")
    elif user_input2 == 'no':
        print("then, you have it now!")

