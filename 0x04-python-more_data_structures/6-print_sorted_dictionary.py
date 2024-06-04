#!/usr/bin/python3

"sorted by keys"

def print_sorted_dictionary(a_dictionary):
    for key in sorted(a_dictionary):
        print("{}:{}".format(key, a_dictionary[key]))
