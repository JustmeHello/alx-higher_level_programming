#!/usr/bin/python3
"""
Defines a Square class.
"""



class Square:
    """
    Represents a square.


    Attributes:
        __size (int): The size of the square.
    """


    def __init__(self, size=0):
        """
        Initializes anew square.

        Args:
            size (int, optional): The size of the square Defaults to 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
if __name__ = "__main__":
    my_square_1 = Square(3)
    print(type(my_square_1))
    print(my_square_1.__dict__)


    my_square_2 = Square()
    print(type(my_square_2))
    print(my_square_2.__dict__)


    try:
        print(my_square_1.size)
    except Exception as e:
        print(e)
    
    try:
        print(my_square_1.__size)
    except Exception as :
        print(e)

    try:
        my_square_3 = Square("3")
        print(type(my_sqaure_3))
        print(my_square_3.__dict__)
    except Exception as e:
        print(e)

    try:
        my_square_4 = Square(-89)
        print(type(my_square_4))
        print(my_sqaure_4.__dict__)
    except Exception as e:
        print(e)
