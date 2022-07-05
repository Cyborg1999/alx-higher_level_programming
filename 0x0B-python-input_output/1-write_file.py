#!/usr/bin/python3
""" Method that returns the number of lines of a text file """


def number_of_lines(filename=""):
    """ Method that reads from file and prints it number of lines

    Args:
        filename: filename

    Raises
        Execption: when file can be opened

    """

    n_lines = 0
    with open(filename, 'r', encoding="utf-8") as f:
        for line in f:
            n_lines += 1
    return n_lines
