#!/usr/bin/python3

"reversed list"

def print_reversed_list_integer(my_list=[]):
    for item in my_list[::-1]:
        print("{}".format(item))
