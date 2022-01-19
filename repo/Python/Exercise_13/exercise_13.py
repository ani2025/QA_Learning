#!usr/bin/evn python3

cost = int(input("Enter the cost of your meal: "))
TAX_RATE = 5.2
TIP_RATE = 18
tax = TAX_RATE * cost  / 100
tip = TIP_RATE * cost / 100
total = tax + tip + cost
print("Tax amount is: ", round(tax, 2), "\nTip amount is: ", round(tip, 2), "\nGrand total is: ", round(total, 2))