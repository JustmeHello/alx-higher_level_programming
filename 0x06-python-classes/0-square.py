#!/usr/bin/python3
"""

Defines a Square class.
"""



class Square:
    """
    Respresents a square.


    Attributes:
        No public attributes for now.
    """


    def __init__(self):
        """
        Initializes an empty square.

        Args:
            No arguments for now.
        """
        pass



if __name__ == "__main__":
    my_square = Square()
    print(type(my_square))
    print(my_square.__dict__)
