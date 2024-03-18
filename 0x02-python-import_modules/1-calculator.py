#!/usr/bin/python3
from calculator_1 import add, mul, sub, div
a = 10
b = 5
added = add(a, b)
print("{} + {} = {}".format(a, b,added))

minus = sub(a, b)
print("{} - {} = {}".format(a, b,minus))

pro = mul(a, b)
print("{} * {} = {}".format(a, b, pro))

quo = div(a, b)
print("{} / {} = {}".format(a, b, quo))