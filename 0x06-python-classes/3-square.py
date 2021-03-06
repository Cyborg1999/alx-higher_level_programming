#!/usr/bin/python3
"""Define the class Square"""


class Square:
    """A Class that defines a square by its size
    """
    def __init__(self, size=0):
        """ Method to initialise the square object
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """ Method to calculate the area of a square
            returns the value area
        """
        return (self.__size ** 2)
