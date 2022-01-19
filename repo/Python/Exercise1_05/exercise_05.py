#!/usr/bin/env python3

height = int(input("Enter the height of a diamond: "))

for i in range (0, height):
    print(" " * (height - i) + "*" * (2 * i + 1))
    
for i in range(-height + 1, 0):
    print (" " * (height + 1 + i) + "*" * (-2 * i - 1))