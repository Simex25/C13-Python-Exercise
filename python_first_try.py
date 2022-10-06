# Calculate the area and circumference of a circle from it's radius.
# Step 1: Prompt for a radius.
# Step 2: Apply the area formular.
# Step 3: Print out the result.


import math

if __name__ == '__main__':
    radius_str = input("Enter the radius of your choice: ")
    radius_int = int(radius_str)

    circumference = 2 * math.pi * radius_int
    area = math.pi * (radius_int ** 2)

    print("The circumference is:", circumference, ", and t"
                                                  ""
                                                  "he area is:", area)