import math


class assignment2:
    @staticmethod
    def twelve_day():
        day = int(input('Enter any day between 1 - 12: '))
        if day >= 1 or day <= 12:
            match day:
                case 12:
                    print("On the twelfth day of Christmas, my true love sent to me\n" +
                          "Twelve drummers drumming\n" +
                          "Eleven pipers piping\n" +
                          "Ten lords a-leaping\n" +
                          "Nine ladies dancing\n" +
                          "Eight maids a-milking\n" +
                          "Seven swans a-swimming\n" +
                          "Six geese a-laying\n" +
                          "Five gold rings (five golden rings)\n" +
                          "Four calling birds\n" +
                          "Three French hens\n" +
                          "Two turtledoves\n" +
                          "And a partridge in a pear tree")

                case 11:
                    print("On the eleventh day of Christmas, my true love sent to me\n" +
                          "I sent eleven pipers piping\n" +
                          "Ten lords a-leaping\n" +
                          "Nine ladies dancing\n" +
                          "Eight maids a-milking\n" +
                          "Seven swans a-swimming\n" +
                          "Six geese a-laying\n" +
                          "Five gold rings (five golden rings)\n" +
                          "Four calling birds\n" +
                          "Three French hens\n" +
                          "Two turtledoves\n" +
                          "And a partridge in a pear tree")

                case 10:
                    print("On the tenth day of Christmas, my true love sent to me\n" +
                          "Ten lords a-leaping\n" +
                          "Nine ladies dancing\n" +
                          "Eight maids a-milking\n" +
                          "Seven swans a-swimming\n" +
                          "Six geese a-laying\n" +
                          "Five gold rings (five golden rings)\n" +
                          "Four calling birds\n" +
                          "Three French hens\n" +
                          "Two turtledoves\n" +
                          "And a partridge in a pear tree")
                case 9:
                    print("On the ninth day of Christmas, my true love sent to me\n" +
                          "Nine ladies dancing\n" +
                          "Eight maids a-milking\n" +
                          "Seven swans a-swimming\n" +
                          "Six geese a-laying\n" +
                          "Five gold rings (five golden rings)\n" +
                          "Four calling birds\n" +
                          "Three French hens\n" +
                          "Two turtledoves\n" +
                          "And a partridge in a pear tree")

                case 8:
                    print("On the eighth day of Christmas, my true love sent to me\n" +
                          "Eight maids a-milking\n" +
                          "Seven swans a-swimming\n" +
                          "Six geese a-laying\n" +
                          "Five gold rings (five golden rings)\n" +
                          "Four calling birds\n" +
                          "Three French hens\n" +
                          "Two turtledoves\n" +
                          "And a partridge in a pear tree")

                case 7:
                    print("On the seventh day of Christmas, my true love sent to me\n" +
                          "Seven swans a-swimming\n" +
                          "Six geese a-laying\n" +
                          "Five gold rings (five golden rings)\n" +
                          "Four calling birds\n" +
                          "Three French hens\n" +
                          "Two turtledoves\n" +
                          "And a partridge in a pear tree")

                case 6:
                    print("On the sixth day of Christmas, my true love sent to me\n" +
                          "Six geese a-laying\n" +
                          "Five gold rings (five golden rings)\n" +
                          "Four calling birds\n" +
                          "Three French hens\n" +
                          "Two turtledoves\n" +
                          "And a partridge in a pear tree")

                case 5:
                    print("On the fiftieth day of Christmas, my true love sent to me\n" +
                          "Five gold rings (five golden rings)\n" +
                          "Four calling birds\n" +
                          "Three French hens\n" +
                          "Two turtledoves\n" +
                          "And a partridge in a pear tree")

                case 4:
                    print("On the fourth day of Christmas, my true love sent to me\n" +
                          "Four calling birds\n" +
                          "Three French hens\n" +
                          "Two turtledoves\n" +
                          "And a partridge in a pear tree")
                case 3:
                    print("On the third day of Christmas, my true love sent to me\n" +
                          "Three French hens\n" +
                          "Two turtledoves\n" +
                          "And a partridge in a pear tree")
                case 2:
                    print("On the second day of Christmas, my true love sent to me\n" +
                          "Two turtledoves\n" +
                          "And a partridge in a pear tree")
                case 1:
                    print("On the first day of Christmas, my true love sent to me\n" +
                          "A partridge in a pear tree")
        else:
            print("enter values between 1 - 12")



    @staticmethod
    def guessing_app():
        user_input = 0
        number = 70
        count = 0

        while user_input != -1:
            user_input = int(input("Guess the number between 1 and 100  :"))
            if user_input > number:
                print("Too high")
            elif user_input < number:
                print("Too low")
            elif user_input == number:
                print(f"Wow you got it right the number is {number}")
                break
            if user_input == 67:
                print("Owww close, go little high")
            if user_input == 72:
                print("Owww close, go a little lower")
            count = count + 1
            if count == 3:
                user_input = int(input("Enter any number to continue or -1 to quit:"))
            if count == 10:
                print("You should be able to do better")
                if user_input == 1:
                    continue
                elif user_input == -1:
                    print("Better luck next time")
                    break
                else:
                    user_input = int(input("Enter any number to continue or -1 to quit:"))

    @staticmethod
    def hypotenuse():
        opp = float(input("Enter for side 1:"))
        adj = float(input("Enter for side 2:"))
        hyp = math.sqrt(math.pow(opp, 2) + math.pow(adj, 2))
        print(f"Hypotenuse : {hyp:.2f}")

    @staticmethod
    def multiples():
        count = 1
        number = int(input("Enter any number to find the multiples:"))
        while count <= number:
            if number % count == 0:
                print(f"{count} is a multiple of {number}")
            count += 1

    @staticmethod
    def temperature():
        kev = float(input("Enter celsius degree"))
        cel = float(input("Enter kelvin degree"))
        kelvin = cel + 273.15
        celsius = kev - 273.15
        print(f"Kelvin degree : {kelvin}")
        print(f"celsius degree : {celsius}")

    @staticmethod
    def sum_of_digits():
        num = input("Enter numbers :")
        num1 = int(num)
        count = 0
        total = 0
        while count <= num1:
            if len(num) == 4:
                rem = num1 % 10
                total += rem
                num1 //= 10
                count += 1
                print(f"The total of the {num} is : {total}")
            elif len(num) > 4:
                print("Length of number must be 4")
                break


    @staticmethod
    def pixel_quantization():
        pix = 0
        pixel = [10, 30, 50, 70, 90, 110, 130, 150, 170, 190]
        num = int(input("Enter any number"))
        if 0 < num <= 20:
            pix = pixel[0]
        if 20 < num <= 40:
            pix = pixel[1]
        if 40 < num <= 60:
            pix = pixel[2]
        if 60 < num <= 80:
            pix = pixel[3]
        if 80 < num <= 100:
            pix = pixel[4]
        if 100 < num <= 120:
            pix = pixel[5]
        if 120 < num <= 140:
            pix = pixel[6]
        if 140 < num <= 160:
            pix = pixel[7]
        if 160 < num <= 180:
            pix = pixel[8]
        if num > 180:
            pix = pixel[9]
        print(pix)


if __name__ == "__main__":
    assignment2.guessing_app()
    assignment2.multiples()
    assignment2.hypotenuse()
    assignment2.temperature()
    assignment2.sum_of_digits()
    assignment2.pixel_quantization()
    assignment2.twelve_day()
