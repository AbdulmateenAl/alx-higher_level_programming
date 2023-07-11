#!/usr/bin/python3
"""Defines a geometry class"""


class BaseGeometry:
    """Represents a base geometry class"""

    def area(self):
        """Area of a geometry: Not implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates an integer

        Args:
            name (str): The name argument
            value (int): The argument to validate.
        Raises:
            TypeError: if value is not an integer.
            ValueError: if value is less than or equal to 0
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
