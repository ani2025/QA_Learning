#!usr/bin/evn python3

height = int(input("Enter the number of rows: "))
for i in range(0, height):
    if i == 0:
        print(" " * (height -1 -i) + "*")
    elif i == (height//2):
        print((height - i - 1) * " " + height * "*" + (height - 1 - i) * " ")
    else:    
        print(" " * (height - i - 1) + "*" + ((2 * i) - 1) * " " + "*")