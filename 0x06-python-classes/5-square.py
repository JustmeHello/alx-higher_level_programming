#!/usr/bin/python3
"""
Defines a Square class.
"""


class Sqaure:
    """
    Represents a square.

    Attributes:
        __size (int): The size of the square;
    """

    def __init__(self, size=0):
        """
        Initializes a new square.

        Args:
            size (int, optional): The size of the square. Defualts to 0.
        """
        self.__size = size
    @size.setter
    def size(self, value):
        """
        Setter method for the size attribute.

        Args:
            value: The value to set for the size attribute.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isistance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
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
    def my_print(self):
        """
        Prints the square with the character '#' to stdout.
        if size is equal to 0, prints an empty line.
        """
        if self.__size ==0;
            print()
        else:
            for _ in range(sself.__size):
                print("#" * self.__size)


if __name__ == "__main__":
    my_square = Square(3)
    my_square.my_print()

    print("--")

    my_square.size = 10
    my_square.my_print()

    print("__")

    my_square.size = 0
    my_square.my_print()

    print("--")
