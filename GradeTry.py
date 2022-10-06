def func_new():
    counter = 0
    while counter < 5:
        grade = int(input('Enter your grade: '))
        if grade < 0 or grade > 100:
            print('Invalid grade!')
        elif grade >= 90 or grade == 100:
            print("A")
        elif grade >= 70:
            print("B")
        elif grade >= 50:
            print("c")
        elif grade >= 40:
            print("D")
        elif grade >= 30:
            print("E")
        else:
            print("F\nOlodo!!")
        counter += 1


if __name__ == '__main__':
    func_new()
