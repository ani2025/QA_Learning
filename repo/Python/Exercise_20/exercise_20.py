#!usr/bin/env python3

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))
num4 = int(input("Enter fourth number: "))
num5 = int(input("Enter fifth number: "))
min_num = num1
max_num = num1
if num2 < min_num:
    min_num = num2
if num3 < min_num:
    min_num = num3
if num4 < min_num:
    min_num = num4
if num5 < min_num:
    min_num = num5
print("Smallest integer is", min_num)
if num2 > max_num:
    max_num = num2
if num3 > max_num:
    max_num = num3
if num4 > max_num:
    max_num = num4
if num5 > max_num:
    max_num = num5  
print("Largest integer is", max_num)