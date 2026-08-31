import math


a = int(input("Enter side a: " ))
b = int(input("Enter side b: " ))
c = int(input("Enter side c: " ))
print("The perimeter of the triangle is ", a + b + c)

length = int(input("Enter the length: "))
width = int(input("Enter the width: "))
print("The perimeter of the rectangle is ", (length + width) * 2)

points = ((2, 2), (6, 10))
slope = (points[1][0] - points[0][0]) / (points[1][1] - points[0][1])
print("The slope is ", slope)

python_len = len("python")
dragon_len = len("dragon")
print("Python does not equal dragon: ", python_len != dragon_len)
print("on" in "python" and "on" in "dragon")


