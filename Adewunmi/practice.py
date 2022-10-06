'''if __name__ == '__main__':
    number = (14 + 6) * 2
    number2 = 14 + 6 * 2
    number3 = 5 // 2
    number4 = 5 / 2

    print(type(number2))

    print(number)
    print(number2)
    print(number3)
    print(number4)

    print('\'Welcome to Python\'')
    print('\\Welcome to Python\\')
    print('\"Welcome to Python\"')
    print('The interpreter reassembles the string’s',
          'parts into a single string with no line break.')

    name = input('What is your name?')
    print('My name is', name)'''

from firstclass import FirstClass


if __name__ == '__main__':
    account = FirstClass('Adewunmi', 16)
    print('My name is ', account.get_name())
    print('I am ', account.get_age(), 'years old')






