#!/usr/bin/python3
""" Class Decscribing the dimensions of class Rectangle """


class Rectangle:
    """ Class that defines a  rectangle """
    def __init__(self, width=0, height=0):
        """ Method that initializes the class

        Args:
            width: rectangle width
            height: rectangle height

        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ Method that returns the value of width

        Returns:
            width

        """

        return self.__width

    @width.setter
    def width(self, value):
        """ Method that defines the width

        Args:
            value: width
        Raises:
            TypeError: if width is not an integer
            ValueError: if value is less than 0

        """

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("widthb must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ Method that returns the value of the height
        Returns:
            height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """ Method that defines teh height of rectangle

        Args:
            value: height
        Raises:
            TypeError: if width is not an integer
            ValueError: if value is less than 0

        """

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ Method that calculates the Rectangular area

        Returns:
            area

        """
        if self.__width == 0 or self.__height == 0:
            return 0

        return self.__width * self.__height

    def perimeter(self):
        """Method to calculate the perimeter of a rectangle

        Returns:
            perimeter

        """
        if self.__width == 0 or self.__height == 0:
            return 0

        return 2 * (self.__width + self.__height)
