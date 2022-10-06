# from math import *
import math

if __name__ == '__main__':
    radius_str = input("Enter the radius of the circle: ")
    radius_int = int(radius_str)

    circumference = 2 * math.pi * radius_int
    area = math.pi * (radius_int ** 2)
    print("The circumference is:", round(circumference, 2),
          "\n and the area is:", round(area, 2))
    # to approximate to decimal number,  "\and the area is:",round (area, 2)
    print('*\n ' * 10)


    print(4.0 // 4.0)
