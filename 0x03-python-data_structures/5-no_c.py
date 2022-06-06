#!/usr/bin/python3
from calendar import c


def no_c(my_string):
    return ''.join(c for c in my_string if c not in 'cC')