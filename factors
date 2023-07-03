#!/usr/bin/python3
import sys


def factorize(Num):
     """Create 2 factors for a given number"""

    factors = []
    i = 2

    while i * i <= NUM:
        if NUM % i:
            i += 1
        else:
            NUM //= i
            factors.append(i)
    if NUM > 1:
        factors.append(NUM)
    return factors

def main():

    if len(sys.argv) != 2:
        print("Usage: factors <file>")
        return

    filename = sys.argv[1]

    try:
        with open(filename, 'r') as file:
            for line in file:
                NUM = int(line.strip())
                factors = factorize(NUM)
                p = factors[0]
                q = NUM // p
                print(f"{NUM}={p}*{q}")

    except FileNotFoundError:
        print(f"File '{filename}' not found.")

    except ValueError:
        print("Invalid NUM in the file.")


if __name__ == "__main__":
    main()
