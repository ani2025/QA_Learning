#!/usr/bin/env python3

price = int(input("Enter the price of meal: "))
tip = int(input("Enter the percent tip you want to leave: "))
print("The tip amount is", price * tip / 100)
print("Total amount is", price + price * tip / 100)