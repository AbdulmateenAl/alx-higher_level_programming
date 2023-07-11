#!/usr/bin/python3
"""Defines a class that inherits from list"""


class MyList(list):
    """Represents the MyList class"""

    def print_sorted(self):
        """Function prints a sorted list"""
        print(sorted(self))
