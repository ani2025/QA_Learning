#!/usr/bin/env python3

list_of_numbers = []
elements = input("Enter the elements of list: ").split()

for item in elements:
    item = int(item)
    list_of_numbers.append(item)

if len(list_of_numbers) >= 0 and list_of_numbers== sorted(list_of_numbers) or list_of_numbers == sorted(list_of_numbers, reverse = True):
    print("The list is sorted")   
else:
    print ("The list is not sorted")