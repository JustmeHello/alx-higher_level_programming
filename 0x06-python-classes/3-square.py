#!/usr/bin/python3
"""
Defines a Square class.
"""


class Square:
    """
    Represents a square.

    Attributes:
        __size (int): the size of the square.
    """


    def __init__(self, size=0):
        """
        Initializes a new square.

        Args:
            size (int, optional): The size of the square. Defaults to 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
    def area(self):
        """
        Computes and returns the area of the sqaure.

        Returns:
            int: The area of the sqaure.
        """
        return self.__size ** 2
if __name__ == "__main__":
    my_square_1 = Square(3)
    print("Area: {}".format(my_square_1.area()))


    try:
        print(my_square_1.size)
    except Exception as e:
        print(e)

    try:
        print(my_square_1.__size)
    except Exception as e:
        print(e)


    my_square_2 = Square(5)
    print("Area: {}".format(my_sqaure_2.area()))
