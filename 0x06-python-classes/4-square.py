#!/usr/bin/python3
"""Define class Square"""


class Square:
    """ Define Square by its Size
    """
    def __init__(self, size=0):
        """Initialize the attributes of the square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError(" size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """ Method that returns the area of the square object
        """
        return((self.__size) * (self.__size))

    @property
    def size(self):
        """ Method that return the size of the value
        """
        return self.__size

    @size.setter
    def size(self, value):
        """ Method to set the size value of square object
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError(" size must be >= 0")
        else:
            self.__size = value
