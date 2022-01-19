#!usr/bin/evn python3
num1 = int(input("Enter a first number: "))
num2 = int(input("Enter a second number: "))
if num1 % num2 == 0:
    print(num1, "is a multiple of the", num2)
else:
    print(num1, "is not a multiple of the", num2)