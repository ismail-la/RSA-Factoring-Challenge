#!/usr/bin/python3
import sys
def factorize(num):
    """Factorize as many numbers as possible into a product of two smaller numbers"""

    factors = []
    Fact = 2

    while Fact * Fact <= num:
        if num % Fact:
            Fact += 1
        else:
            num //= Fact
            factors.append(Fact)
    if num > 1:
        factors.append(num)
    return factors

def main():
    """main function"""

    if len(sys.argv) != 2:
        print("Usage: factors <file>")
        return

    filename = sys.argv[1]
    try:
        with open(filename, 'r') as file:
            for line in file:
                num = int(line.strip())
                factors = factorize(num)
                p = factors[0]
                q = num // p
                print(f"{num}={p}*{q}")
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
    except ValueError:
        print("Invalid number in the file.")

if __name__ == "__main__":
    main()
