#!/usr/bin/env python3

list_of_words = []
word = input("Enter the words(enter a blank to exit): ")

while word != "":
    if word not in list_of_words:
        list_of_words.append(word)
    word = input("Enter the words(enter a blank to exit): ")
for item in list_of_words:
    print(item)