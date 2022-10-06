if __name__ == '__main__':
    numbers = 0
    print("%4s%30s" % ("Hour", "Number of bacterial"))
    for hour in range(0, 20, 5):
        numbers = 200 * 2 * hour
        print("%d%30d" % (hour, numbers))
