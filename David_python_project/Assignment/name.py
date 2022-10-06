if __name__ == '__main__':
    grade = int(input("Enter a grade: "))
    while 0 <= grade <= 100:
        if grade >= 90:
            print("A\n'Congratulations! Your grade of 91 earns you an A in this course.'")
            break
        if 80 <= grade < 90:
            print("B\nGood try.")
            break
        if 70 <= grade < 80:
            print("B\nGood try")
            break
        if 60 <= grade < 50:
            print("C\nAlmost there.")
            break
        else:
            print("Your performance is poor\nWrite the exam again!!!")
            break
