#!/usr/bin/python3
""" Print list of objects  """


class MyList(list):
    """ Class that inherits the attributes references of class list

    Args:
        list: class list

    """

    def print_sorted(self):
        """ Method that prints the sorted list """
        print(sorted(self))
