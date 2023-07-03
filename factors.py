#!/usr/bin/python3

import sys


def factorize(the_number):

    """Create 2 factors for a given number."""

    Fact1 = 2

    while (the_number % Fact1):
        if (Fact1 <= the_number):
            Fact1 += 1

    Fact2 = the_number // Fact1
    return (Fact2, Fact1)


if len(sys.argv) != 2:
    sys.exit(f"Wrong usage: {sys.argv[0]} <file_path>")

filename = sys.argv[1]
file = open(filename, 'r')
lines = file.readlines()


for line in lines:
    the_number = int(line.rstrip())
    Fact2, Fact1 = factorize(the_number)
    print(f"{the_number} = {Fact2} * {Fact1}")
