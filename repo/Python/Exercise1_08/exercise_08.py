#!/usr/bin/env python3

print ("Original_prices", "\t", "Discount", "\t","Prices_after_discount")

discount = 0.6
original_prices = [4.95, 9.95, 14.95, 19.95, 24.95]

for item in (original_prices):
    discount_list = discount * item
    new_prices = item - discount * item
    print(item, 3 * "\t", format(discount_list, ".2f"), 3 * "\t", format(new_prices, ".2f"))
