#!/usr/bin/python3
"""
Defines a Square class.
"""


class Square:
    """
    Represents a square.

    Attributes:
        __size (float or int): The size of the square.
    """

    def __init__(self, size=0):
        """
        Initializes a new square.

        Args:
            size (float or int, optional): The size of the square. Defaults to 0.
        """
        self.size = size

    @property
    def size(self):
        """
        Getter method for the size attribute.

        Returns:
            float or int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter method for the size attribute.

        Args:
            value: The value to set for the size attribute.

        Raises:
            TypeError: If value is not a number (float or integer).
            ValueError: If value is less than 0.
        """
        if not isinstance(value, (float, int)):
            raise TypeError("size must be a number")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """
        Computes and returns the area of the square.

        Returns:
            float or int: The area of the square.
        """
        return self.__size ** 2

    def __eq__(self, other):
        """
        Equal comparison method.

        Args:
            other (Square): The other square to compare.

        Returns:
            bool: True if the areas are equal, False otherwise.
        """
        return self.area() == other.area()

    def __ne__(self, other):
        """
        Not equal comparison method.

        Args:
            other (Square): The other square to compare.

        Returns:
            bool: True if the areas are not equal, False otherwise.
        """
        return self.area() != other.area()

    def __lt__(self, other):
        """
        Less than comparison method.

        Args:
            other (Square): The other square to compare.

        Returns:
            bool: True if the area is less than the other's area, False otherwise.
        """
        return self.area() < other.area()

    def __le__(self, other):
        """
        Less than or equal comparison method.

        Args:
            other (Square): The other square to compare.

        Returns:
            bool: True if the area is less than or equal to the other's area, False otherwise.
        """
        return self.area() <= other.area()

    def __gt__(self, other):
        """
        Greater than comparison method.

        Args:
            other (Square): The other square to compare.

        Returns:
            bool: True if the area is greater than the other's area, False otherwise.
        """
        return self.area() > other.area()

    def __ge__(self, other):
        """
        Greater than or equal comparison method.

        Args:
            other (Square): The other square to compare.

        Returns:
            bool: True if the area is greater than or equal to the other's area, False otherwise.
        """
        return self.area() >= other.area()


if __name__ == "__main__":
    Square = __import__('102-square').Square

    s_5 = Square(5)
    s_6 = Square(6)

    if s_5 < s_6:
        print("Square 5 < Square 6")
    if s_5 <= s_6:
        print("Square 5 <= Square 6")
    if s_5 == s_6:
        print("Square 5 == Square 6")
    if s_5 != s_6:
        print("Square 5 != Square 6")
    if s_5 > s_6:
        print("Square 5 > Square 6")
    if s_5 >= s_6:
        print("Square 5 >= Square 6")

