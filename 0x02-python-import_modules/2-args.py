#!/usr/bin/python3
from sys import argv

if len(argv) == 1:
    print("0 arguments.")
elif len(argv) == 2:
    print("1 argument:")
else:
    print("{:d} arguments:".format(len(argv) - 1))

for i in range(1, len(argv)):
    print("{:d}: {:s}".format(i, argv[i]))
