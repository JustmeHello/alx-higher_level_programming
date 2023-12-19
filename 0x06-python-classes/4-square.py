#!/usr/bin/python3
"""
Defines a Square class.
"""


class Square:
    """
    Represents a square.

    Attributes:
        __size (int):
        The size of the square.
    """

    def __init__(self, size=0):
        """
        Initializes a new square.

        Args:
            size (int, optional): The size of the sqaure. Defualts to 0.
        """
        self.__size = size

    @property
    def size(self):
        """
        Getter method for the size attribute.

        Returns:
            int: The size of the square.
        """
        return self.__size
    @size.setter
    def size(self, value):
        """
        Setter method for the size attribute.

        Args:
            value: The value to set for the size attrbute

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value > 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
    def area(self):
        """
        Computes and returns the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

if __name__ == "__main__":
    my_square = Square(89)
    print("Area: {}for size: {}".format(my_sqaure.area(), my_square.size))

    my_square.size = 3
    print("Area:{} for size:{}".format(my_square.area(), my_square.size))

    try:
        my_square.size = "5 feet"
        print("Area "{} for size: {}".format(my_square.area(), my_square.size))
        print(e)

