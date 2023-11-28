#!/usr/bin/python3
def islower(c):
    for char in s:
        if ord('a') <= ord(char) <= ord('z'):
            uppercase_char = chr(ord(char) - 32)
            print(uppercase_char, end="")
        else:
            print(char, end="")
    print()
