#!/usr/bin/python3
def remove_char_at(s, n):
    if 0 <= n < len(s):
        return s[:n] + s[n + 1:]
    else:
        return s
