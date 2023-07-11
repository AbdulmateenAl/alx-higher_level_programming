#!/usr/bin/python3
"""Defines a class checking function"""


def is_kind_of_class(obj, a_class):
    """Represents a class checking function

    Args:
        obj (any): The object to check.
        a_class (type): The class to compare with.

    Return:
        True - If there's a match.
        False - If there is none.
    """
    if isinstance(obj, a_class):
        return True
    return False
