#!/usr/bin/python3
"""Defines a class Rectangle that inherits from BaseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Represents a rectangle"""

    def __init__(self, width, height):
        """Intializes a new rectangle

        Args:
            width (int): The width of the rectangle
            height (int): The height of the rectangle
        """
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """Area of a geometry"""
        return self.__width * self.__height

    def __str__(self):
        """Returns the print() and str() representation of the rectangle"""
        strg = "[" + str(self.__class__.__name__) + "] "
        strg += str(self.__width) + "/" + str(self.__height)
        return strg
