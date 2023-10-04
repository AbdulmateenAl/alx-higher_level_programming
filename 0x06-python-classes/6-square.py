#!/usr/bin/python3

class Square:
    
    def __init__(self, size=0, position=(0,0)):
        self.__size = size
        self.__position = position

    @property
    # Used a getter
    def size(self):
        return self.__size
    
    @size.setter
    # Used a setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        
        self.__size = value

    @property
    # Used a getter
    def position(self):
        return self.__position
    
    @position.setter
    # Used a setter
    def position(self, value):
        if not isinstance(value, tuple) and len(value) != 2:
            raise TypeError("Position must be a tuple of 2 positive integers")

        self.__position = value

    def area(self):
        return self.__size ** 2
    
    def my_print(self):
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
