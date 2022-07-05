#!/usr/bin/python3
""" Module that contains a function that returns the JSON
representation of an object
"""

import json


def save_to_json_file(my_obj, filename):
    """
        writes an object to a text file
        uses JSON representation
        Args:
            my_obj: object to be encoded
            filename: file to be written to
    """
    with open(filename, 'w+') as f:
        json.dump(my_obj, f)
