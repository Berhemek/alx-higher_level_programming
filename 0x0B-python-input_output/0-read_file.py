#!/usr/bin/python3
""" Module that contains a function that reads from a file """


def read_file(filename=""):
    """ Function that reads from a file """

    with open(filename, encoding="utf-8") as f:
        print(f.read(), end='')
