#!/usr/bin/env python3

number1, number2, number3 = (input("Input three different integers: ").split())
number1 = int(number1)
number2 = int(number2)
number3 = int(number3)
sum = number1 + number2+ number3
average = round(sum / 3, 2)
product = number1 * number2 * number3

largest = number1
if number2 > largest:
    largest = number2
if  number3 > largest:
    largest = number3

smallest = number1
if number2 < smallest:
    smallest = number2
if number3 < smallest:
    smallest = number3
    
print("Sum is", sum), print("Average is", average), print("Product is", product), print("Smallest is", smallest), print("Largest is", largest)