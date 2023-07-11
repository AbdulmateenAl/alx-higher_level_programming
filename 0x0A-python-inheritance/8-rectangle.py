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
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
