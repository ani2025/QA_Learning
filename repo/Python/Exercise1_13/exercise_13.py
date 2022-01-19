#!/usr/bin/env python3

list_of_divisors = []
integer_1 = int(input("Enter an integer: "))

for i in range(1, integer_1 // 2 + 1):
    if integer_1 % i == 0:
        list_of_divisors.append(i)
print(list_of_divisors)