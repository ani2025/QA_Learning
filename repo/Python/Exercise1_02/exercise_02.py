#!/usr/bin/env python3

rows = int(input("Enter the number of rows: "))
columns  = int(input("Enter the number of columns: "))

for i in range(rows):
    if i == 0 or i == (rows - 1):
        print("*" * columns)
    else: 
        print("*" + (columns - 2) * " " + "*")  