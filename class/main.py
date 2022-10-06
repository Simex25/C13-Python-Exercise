if __name__ == '__main__':
    x = [45, 76, 81, 90, 67]
    total = 0
    for r in x:
        total += r
    average = total / len(x)
    maximum_grade = max(x)
    minimum_grade = min(x)
    print("Average = {}\nMaximum grade = {}"
          "\nMinimum grade = {}"
          .format(average, maximum_grade, minimum_grade))
    for counter in range(10):
        print(counter, end=' ')
