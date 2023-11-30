#!/usr/bin/python3
from sys import argv
from calculator_1 import add, sub, mul, div

if len(argv) != 4:
    print("Usage: ./100-my_calculator.py <a> <operator> <b>")
    exit(1)

a = int(argv[1])
operator = argv[2]
b = int(argv[3])

if operator not in ('+', '-', '*', '/'):
    print("Unknown operator. Available operators: +, -, * and /")
    exit(1)

result = 0
if operator == '+':
    result = add(a, b)
elif operator == '-':
    result = sub(a, b)
elif operator == '*':
    result = mul(a, b)
elif operator == '/':
    result = div(a, b)

print("{:d} {:s} {:d} = {:d}".format(a, operator, b, result))
