class Assignment:
    @staticmethod
    def digits_list(value):
        digits = []
        counter = 0
        new_value = len(str(value))
        for numbers in range(new_value, -1, -1):
            digits[counter] += numbers
            new_value -= 1
            counter += 1
        return digits

    @staticmethod
    def element_in(value, my_list):
        count = 0
        for element in my_list:
            if element == value:
                print(value, 'is at Index position: ', count)
                count = count + 1
            else:
                print('Index position: ', count)
                count = count + 1

    @staticmethod
    def largest(largest_number):
        maximum = largest_number[0]
        for number in largest_number:
            if number > maximum:
                maximum = number
        print(maximum)

    @staticmethod
    def palindrome_string(words):
        new_value = words[::-1]
        if words == new_value:
            return "This is a palindromic word"
        else:
            return "This is not a palindromic word"

    @staticmethod
    def list_reverse(items):
        length = len(items)
        new_list = []
        count = 0
        for char in range(length, 0, -1):
            new_list.append(char)
        length -= 1
        count += 1
        return new_list

    @staticmethod
    def total_list(values):
        total = 0
        for value in values:
            total += value
        return total

    @staticmethod
    def total_loops(array):
        sum_for_loop = 0
        for j in array:
            sum_for_loop += j
        print(sum_for_loop)

        sum_while_loop = 0
        i = 0
        while i < len(array):
            sum_while_loop += array[i]
            i += 1
        print(sum_while_loop)

    @staticmethod
    def concat(list1, list2):
        return list1 + list2

    @staticmethod
    def validate_even_odd(values_list):
        count = 0
        for value in values_list:
            if value % 2 == 0:
                print(value, " is even at index", count)
                count += 1
            if value % 2 != 0:
                print(value, " is odd at index", count)
                count += 1

    @staticmethod
    def check_in(value, my_list):
        count = 0
        for element in my_list:
            if element == value:
                print(value, 'is  in the list at Index position: ', count)
                break
            else:
                print(value, " is not in the list")
            count = count + 1

    @staticmethod
    def concat2(value1, value2):
        total = []
        index = 0
        length = len(value1 + value2)
        while index < length:
            if index % 2 == 0:
                total.append(value1[index])
            if index % 2 != 0:
                total.append(value2[index])
            index += 1

        return total


if __name__ == '__main__':
    # print(Assignment.digits_list(1234567))
    # Assignment.element_in(25, [1, 2, 3, 4, 5, 6])
    # Assignment.largest([1, 32, 34, 56, 32, 6, 35])
    # print(Assignment.palindrome_string("madam"))
    # print(Assignment.list_reverse([1, 2, 3, 4, 5, 6]))
    # print(Assignment.total_list([1, 2, 3, 4, 5, 6]))
    # print(Assignment.total_loops([1, 2, 3, 4, 5, 6]))
    # print(Assignment.concat([1, 2, 3, 4, 5, 6], ['a','b','c','d','e','f','g','h','i']))
    # print(Assignment.validate_even_odd([1, 2, 3, 4, 5, 6]))
    # Assignment.check_in(3, [1, 2, 3, 4, 5])
    print(Assignment.concat2([1, 2, 3, 4, 5, 6], [7,8,9]))
