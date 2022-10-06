def grade():
    i = 0
    while i < 5:
        grade = int(input("Enter grade: "))

        while 100 < grade or grade < 0:
            grade = int(input("Grade bound exceeded\nEnter score again: "))

        if grade >= 90:
            print("A")
        elif grade >= 70:
            print("B")
        elif grade >= 50:
            print("C")
        elif grade >= 40:
            print("D")
        elif grade >= 30:
            print("E")
        else:
            print("Zero Talent")
        i += 1


if __name__ == '__main__':
    grade()
