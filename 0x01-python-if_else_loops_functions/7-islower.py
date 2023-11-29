#!/usr/bin/python3
def islower(c):
    modified_string = ""
    for char in c:
        if ord('a') <= ord(char) <= ord('z'):
            uppercase_char = chr(ord(char) - 32)
            modified_string += uppercase_char
        else:
            modified_string += char
    return modified_string
