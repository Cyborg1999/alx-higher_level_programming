#!/usr/bin/python3
""" Magic Class """


def magic_string():
    """ Magic Strings 
    Returns:
        print 
    """
    
    magic_string.n = getattr(magic_string, 'n', 0) + 1
    return ("BestSchool," * (magic_string.n - 1) + "BestSchool")
