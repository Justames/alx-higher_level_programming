#!/usr/bin/python3
import random
number = random.randint(-1000, 1000)
last = number % 10
if (last > 5):
    print("last digit of", number, "is", last, "and is greater than 5")
elif (last == 0):
    print("last digit of", number, "is", last, "and is 0")
elif (last < 6):
    print("last digit of", number, "is", last, "and is less than 6 and not 0")
