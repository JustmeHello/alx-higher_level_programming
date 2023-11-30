#!/usr/bin/python3
from sys import argv
from decimal import Decimal

def add_argv():
    if len(argv) == 1:
        print("0")
        return
    total = sum(Decimal(arg) for arg in argv[1:] if arg.replace('.', '', 1).isdigit())
    print(f"{total}")

# Call the function if the script is executed
if __name__ == "__main__":
    add_argv()
