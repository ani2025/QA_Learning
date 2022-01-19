#!usr/bin/evn python3

print ("Celsius", "\t", "Fahrenheit")
for i in range (0, 101, 10):
        fahrenheit = i * 9 / 5 + 32
        print(i, "C", 2 * "\t", fahrenheit, "F")