#!/usr/bin/python3
# 101-locked_class.py
""" Defines a locked class """


class LockedClass:
    """
    Prevent the user from instantiating new LockedClass attributes
    for anything but attributes called 'first_name'
    """

    __slot__ = ["first_name"]

    def __init__(self):
        """ init method """
        pass
