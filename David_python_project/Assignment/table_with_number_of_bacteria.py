print(f"%s" % 'Hour', "%20s" % 'Number of bacteria')
number_of_bacteria = 0;
while number_of_bacteria < 4:
    print(f"%4d" % (number_of_bacteria * 5), "%20d" % (200 * 2 ** (number_of_bacteria * 5)))
    number_of_bacteria += 1



