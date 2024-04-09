#!/usr/bin/python3
""" Write a program that prints all possible different combinations of two digits. 01 and 10 are considered the same combination of the two digits 0 and 1"""
for i in range(0, 9):
    for j in range(i + 1, 10):
        if i == 8 and j == 9:
            print("{}{}".format(i, j))
        else:
            print("{}{}".format(i, j), end=", ")

