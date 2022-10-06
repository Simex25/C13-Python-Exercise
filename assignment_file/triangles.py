def is_valid_triangle(a, b, c):
    if a + b >= c and b + c >= a and c + a >= b:
        return True
    else:
        return False


def triangle_type(a, b, c):
    if a == b and b == c:
        print("The Triangle is Equilateral.")
    else:
        print("The Triangle is not Equilateral.")


if __name__ == '__main__':
    first_side = int(input("Enter first length: "))
    second_side = int(input("Enter second length: "))
    third_side = int(input("Enter first length: "))

    if is_valid_triangle(first_side, second_side, third_side):
        triangle_type(first_side, second_side, third_side)

