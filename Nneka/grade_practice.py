# 90 - 100  A
# 70 - 89   B
# 50 - 69   C
# 40 - 49   D
# 3o - 39   E
# less than 30 ( zero talent)
# promt
# counter = 0
# while counter < 3
# if  user_input < 0
# print Re-enter a number

def grade():
    user_input = input("Enter grade")
    user_input = int(user_input)

    counter = 0
    while counter < 3:
        counter += 1
        if user_input < 0:
            user_input = input("Re-enter a number")
            user_input = int(user_input)
            continue
        else:
            if 90 <= user_input <= 100:
                print ("A")
            elif 70 <= user_input <= 89:
                print("B")
            elif 50 <= user_input <= 69:
                print("C")
            elif 40 <= user_input <= 49:
                print ("D")
            elif 30 <= user_input <= 39:
                print("E")
            else:
                print("You need cane")
            break


if __name__ == '__main__':
    grade()
