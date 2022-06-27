#!/usr/bin/python3
""" Class Decscribing the dimensions of class Rectangle """


class Rectangle:
    """ Class that defines a  rectangle """

    def __init__(self, width=0, height=0):
        """ Method to initialize the class

        Args:
            width: width of rectangle
            height: height of rectangle

        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """  Method that returns value width
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
            ValueError: if width is less than zero

        """
        if not isinstance(value, int):
            raise TypeError("widthmust be an integer")
        if value < 0:
            raise ValueError("width  must be >= 0")
        self.__width = value

        @property
        def height(self):
            """ Method that returns the value of height
            Returns:
                height
            """

            return self.__height

        @height.setter
        def height(self, value):
            """ Method that defines the height
            Args:
                value: height
            Raises:
                TypeError: if height is an int
                ValueError: if the value is less than 0
            """
            if not isinstance(value, int):
                raise TypeError("height must be an integer")
            if value < 0:
                raise ValueError("height must be >= 0")
            self.__height = value

        def area(self):
            """ Method that calculates the area

            Returns:
                area
            """

            return self.__width * self.__height

        def perimeter(self):
            """ Method to calculate the perimeter

            Returns:
                perimeter
            """
            if self.__width == 0 or self.__height == 0:
                return 0
            return 2 * (self.__width + self.__height)

        def __str__(self):
            """ Method that returns the Rectangle #

            Returns:
                str of the rectangle

            """

            rectangle = ""

            if self.__width == 0 or self.__height == 0:
                return rectangle

            for i in range(self.__height):
                rectangle += ("#" * self.__width) + "\n"

            return rectangle
