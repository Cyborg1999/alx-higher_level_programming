#!/usr/bin/python3
""" Define class Square"""


class Square:
    """ Class that defines a Square by its size
    """
    def __init__(self, size=0):
        """ Method to initialize the square of the object
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """ Method to calculate area
        """
        return (self.__size ** 2)

    @property
    def size(self):
        """Method to return the size value
        """
        return self.__size
    
    @size.setter
    def size(self, value):
        """ Class that sets the vslue of the square object
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def my_print(self):
        """ Method to prints a # square according to the size value
        """
        if not self.__size:
            print()
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end='')
                print()
