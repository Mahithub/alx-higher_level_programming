#!/usr/bin/python3
if __file__ == "__main__":

from calculator_1 import add, div, mul, sub
    a = 10
    b = 5
    
    print("{} + {} = {}".format(a, b, add(a, b)))
    print("{} / {} = {}".format(a, b, div(a, b)))
    print("{} * {} = {}".format(a, b, mul(a, b)))
    print("{} - {} = {}".format(a, b, sub(a, b)))
