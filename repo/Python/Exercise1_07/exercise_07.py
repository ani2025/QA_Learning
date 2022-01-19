#!/usr/bin/env python3

count = 0 
sum = 0
values = int(input("Enter a value (enter 0 to exit): "))

while values != 0:
    sum = sum + values
    count += 1   
    values = int(input("Enter a value (enter 0 to exit): "))

average = sum / count
print(f"Average of the values is {round(average, 2)}")