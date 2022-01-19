#!usr/bin/evn python3

first_number = int(input("Enter a number: "))
second_number = int(input("Enter another number: "))
if first_number > second_number:
    print(first_number, "is larger.")
elif second_number > first_number:
    print(second_number, "is larger.")  
else:
    print("These numbers are equal.")  