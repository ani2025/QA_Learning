#!usr/bin/evn python3

radius = int(input("Enter a radius of a circle: "))
PI = 3.14159
print("Circle's diameter is", 2 * radius)
print("Circle's circumference is", round(2 * PI * radius, 2))
print("Circle's area is", round(PI * radius ** 2, 2))