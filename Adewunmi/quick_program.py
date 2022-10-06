# calculate the area and circumference of a circle from its radius.
# Step 1: prompt a radius
# Step 2: Apply the area formula
# Step 3: Print the results


import math

if __name__ == '__main__':

    radius_str = input("Enter the radius of the circle: ")
radius_int = int(radius_str)

circumference = 2 * math.pi * radius_int
area = math.pi * (radius_int ** 2)

print("The circumference is: ", circumference,
      "\n and the area is : ", area)


