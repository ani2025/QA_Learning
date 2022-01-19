#!usr/bin/evn python3

number_1 = float(input("Enter the number of containers holding one liter or less: "))
number_2 = float(input("Enter the number of containers holding more than one liter: "))
print("Your deposit for containers is", round(number_1 * 0.10, 2) + round(number_2 * 0.25, 2), "$")