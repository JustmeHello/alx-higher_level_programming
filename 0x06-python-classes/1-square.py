#!/usr/bin/python3
"""
Defines a Square class.
"""



class Square:
    """
    Represents a square.

    Attributes:
        __size (init): The size of the square.
    """


    def __init__(self, size):
        """
        Initializes a new square.

        Args:
            size (int): The size of the square.
        """
        self.__size = size


if __name__ == "__main__":
    my_square = Square(3)
    print(type(my_square))
    print(my_square.__dict__)

    try:
        print(my_square.size)
    except Exception as e:
        print(e)

    try:
        print(my_square.__size)
    except Exception as e:
        print(e)
