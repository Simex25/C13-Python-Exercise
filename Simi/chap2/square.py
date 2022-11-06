class ClassWork:

    @staticmethod
    def dict_num1():
        number = int(input("Number"))
        dict_num = {}
        for i in range(1, number + 1):
            dict_num[i] = i * i
        print(dict_num)

    @staticmethod
    def user():
        count = 1
        num_set = set()

        while count <= 5:
            try:
                user_input = int(input("Enter your number"))
                if 2 <= user_input <= 90:
                    num_set.add(user_input)
                    count += 1
                print(num_set)
            except ValueError:
                print("Invalid input")

    @staticmethod
    def two_list():
        list1 = ['Ten', 'Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety', 'Hundred']
        list2 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
        dict_items = {}
        count = 0
        for i in list2:
            dict_items[i] = list1[count]
            count += 1
        print(dict_items)


if __name__ == "__main__":
    # ClassWork.dict_num1()
    ClassWork.user()
# ClassWork.two_list()
