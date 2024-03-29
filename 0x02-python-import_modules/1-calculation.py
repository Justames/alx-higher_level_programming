#!/usr/bin/python3
from calculator_1 import add, mul, sub, div
a = 10
b = 5
added = add(a, b)
print(f"{a} + {b} = {added}")

minus = sub(a, b)
print(f"{a} - {b} = {minus}")

pro = mul(a, b)
print(f"{a} * {b} = {pro}")

quo = div(a, b)
print(f"{a} / {b} = {quo}")
