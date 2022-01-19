#!/usr/bin/env python3

list = []
numbers = input("Enter the numbers(blank to exit): ")
list.append(int(numbers))

while numbers != "":
    numbers = input("Enter the numbers(blank to exit): ")  
    if numbers != "":
        list.append(int(numbers))
        
for item in list:
    if item < 0:
        print(item, end = " ")
for item in list:
    if item == 0:
        print(item, end = " ")
for item in list:
    if item > 0:
        print(item, end = " ")