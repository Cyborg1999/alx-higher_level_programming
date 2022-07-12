#!/usr/bin/python3
""" Module that contains Rectangle
inheritance from class Base
"""


from models.base import Base


class Rectangle(Base):
    """ Class Rectangle """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ Initialises the class and instances """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """ Module to get width """
        return self.__width

    @width.setter
    def width(self, value):
        """ Module to set width """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be an integer")
        self.__width = value

    @property
    def height(self):
        """ Module to get height """
        return self.__height

    @height.setter
    def height(self, value):
        """ Module to set height """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """ Module to get x """
        return self.__x

    @x.setter
    def x(self, value):
        """ Module to set x """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value <= 0:
            raise ValueError("x must be > 0")
        self.__x = value

    @property
    def y(self):
        """ Module to get y """
        return self.__y

    @y.setter
    def y(self, value):
        """ Module to set y """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value <= 0:
            raise ValueError("y must be > 0")
        self.__y = value

    def area(self):
        """ return the value of the area of a rectangle """
        return self.__width * self.__height

    def display(self):
        """ display a rectangle """
        rectangle = self.__y * "\n"
        for i in range(self.__height):
            rectangle += (" " * self.__x)
            rectangle += ("#" * self.__width) + "\n"

        print(rectangle, end='')

    def __str__(self):
        """ Special str method """
        str_rectangle = "[Rectangle]"
        str_id = "({})".format(self.id)
        str_xy = "{}/{} - ".format(self.__x, self.__y)
        str_wh = "{}/{}".format(self.__width, self.__height)

        return str_rectangle + str_id + str_xy, str_wh

    def update(self, *args, **kwargs):
        """ Mehtod to update values """
        if args != None and len(args) != 0:
            list_atr = ['id', 'width', 'height', 'x', 'y']
            for i in range(len(args)):
                setattr(self, list_atr[i], args[i])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """ Method that returns a dictionary with properties """
        list_atr = ['id', 'width', 'height', 'x', 'y']
        dict_res = {}

        for key in list_atr:
            dict_res[key] = getattr(self, key)

        return dict_res
