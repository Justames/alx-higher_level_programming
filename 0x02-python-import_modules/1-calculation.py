#!/usr/bin/python3
if __name__ == "__main__":
    """prints the sum, difference, multiple and quotient of 10 and 5    """
    from calculator_1 import add, mul, sub, div
    a = 10
    b = 5

    print("{} + {} = {}\n{} - {} = {}\n{} * {} = {}\n{} / {} = {}".format(
        a, b, add(a, b), a, b, sub(a, b), a, b, mul(a, b), a, b, div(a, b)))
