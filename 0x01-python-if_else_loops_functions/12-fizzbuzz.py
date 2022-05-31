#!/usr/bin/python3
def fizzbuzz():
    for number in range(1, 101):
        if number % 3 == 0 and number % 5 == 0:
            print(f"{number:d} Fizz Buzz".format(number))
        elif number % 3 == 0:
            print(f"{number:d} Fizz".format(number))
        elif number % 5 == 0:
            print(f"{number:d} Buzz".format(number))
        else:
            print(f"{number:d}".format(number))
