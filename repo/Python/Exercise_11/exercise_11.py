#!usr/bin/evn python3
width = float(input("Enter a widht of a field (in feet): "))
lenght = float(input("Enter a lenght of a field (in feet): "))
ACRE = 43560 #square feet
print("The area of a field is", round(width * lenght / ACRE, 2), "acres.")