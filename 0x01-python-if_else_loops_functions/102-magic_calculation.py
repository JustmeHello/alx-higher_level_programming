#!/usr/bin/python3
def magic_calculation(a, b, c):
    if a < b:
        if c <= 0:
            return a - b
        else:
            return a * b - c
    else:
        if c > b:
            return a + b
        else:
            return a * b - c

