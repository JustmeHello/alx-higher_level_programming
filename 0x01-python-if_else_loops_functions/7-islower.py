#!/usr/bin/python3
def toupper(s):
    modified_string = ""
    for char in s:
        if ord('a') <= ord(char) <= ord('z'):
            uppercase_char = chr(ord(char) - 32)
            modified_string += uppercase_char
        else:
            modified_string += char
    return modified_string
