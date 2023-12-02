#!/usr/bin/env python3
def no_c(my_string):
    result_string = ''.join(char for char in my_string if char.lower() not in {'c', 'C'})
    return result_string
