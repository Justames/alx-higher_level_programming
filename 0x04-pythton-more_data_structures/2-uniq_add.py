#!/usr/bin/python3

"fuction that adds all unique ontegers in a list"

def uniq_add(my_list=[]):
    my_set = set(my_list)
    new_list = list(my_set)
    added = sum(new_list)
    return added
