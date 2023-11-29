#!/usr/bin/python3
output = ""
for i in range(ord('a'), ord('z') + 1):
    if i != ord('q') and i != ord('e'):
        output += "{}".format(chr(i))

print(output)
