#!usr/bin/evn python3

number = str(input("Enter a five-digit number: "))
if len(number) == 5:
    print(number[0], number[1], number[2], number[3], number[4], sep = " "*3)
else:
    print("Enter a five-digit number!")