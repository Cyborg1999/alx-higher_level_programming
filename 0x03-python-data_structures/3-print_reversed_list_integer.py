#!/usr/bin/python3
from click import pass_context


def print_reversed_list_integer(my_list=[]):

    if not my_list:
        pass
    else:
        my_list.reverse()
        for i in range(len(my_list)):
            print("{my_list[i]:d}".format(my_list[i]))
