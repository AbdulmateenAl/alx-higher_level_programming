#!/usr/bin/python3

class Square:
    """ Class Square """
    
    def __init__(self, size=0, position=(0,0)):
        """ define initialization 

        Args:
            size: size of square.
            position: position of square.
        """
        self.__size = size
        self.__position = position

    @property
    # Used a getter
    def size(self):
        """ defined a getter for size

        Returns:
            The return is the private size
        """
        return self.__size
    
    @size.setter
    # Used a setter
    def size(self, value):
        """ defined a setter for setter

        Args:
            value: Tkakes in value and makes sure it passes the condition then puts it in private size
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        
        self.__size = value

    @property
    # Used a getter
    def position(self):
        """ defined getter position

        Returns:
            The return is private position
        """
        return self.__position
    
    @position.setter
    # Used a setter
    def position(self, value):
        """ defined setter position

        Args:
            value: Tkakes in value and makes sure it passes the condition then puts it in private size
        """
        if not isinstance(value, tuple) and len(value) != 2:
            raise TypeError("Position must be a tuple of 2 positive integers")

        self.__position = value

    def area(self):
        """ defined Area

        Returns:
            Thesquare of size"""
        return self.__size ** 2
    
    def my_print(self):
        """ defined my_print

        Note:
            This block goes through some conditions
        """
        if self.__size == 0:
            print("")
        else:
            for a in range(self.__size):
                for i in range(self.__position[0]):
                    #for j in range(self.__size):
                    print('{}'.format('_'), end='')
                for j in range(self.__size):
                    print('{}'.format('#'), end='')
                print("")
