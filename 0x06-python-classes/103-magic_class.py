#!/usr/bin/python3
"""Define Magic class"""


import math


class MagicClass:
    """ Magic Class that makes the same bytecodes
    """

    def __init__(self, radius=0):
        """ Initialize the class Magic
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        else:
            self.__radius = radius

    def area(self):
        """Area function calculates the area of the circumference
        """
        return (self.__radius ** 2) * math.pi

    def circumference(self):
        """Calculates the perimeter of the circumference
        """
        return (2 * math.pi) * self
