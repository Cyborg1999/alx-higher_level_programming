#!/usr/bin/python3
def fizzbuzz():
    for number in range(1, 100):
        if number % 3 == 0 and number % 5 == 0:
            print(f"{number:d}. Fizz Buzz")
        elif number % 3 == 0:
            print(f"{number:d}. Fizz")
        elif number % 5 == 0:
            print(f"{number:d}. Buzz")
        else:
            print(f"{number:d}.")
