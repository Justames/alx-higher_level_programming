#!/usr/bin/python3
for i in range(0, 10):
    a = i + 1
    for a in range(i, 10):
        if (a == i):
            continue
        elif (i == 8 and a == 9):
            print("{}{}".format(i, a), end="\n")
        else:
            print("{}{}".format(i, a), end=", ")
