#!/usr/bin/python3

def print_last_digit(number):
    """Print the last digit of a number"""
    digit = (abs(number) % 10)
    if digit < 0:
        didit = -(digit)
    print(digit, end="")
    return(digit)
