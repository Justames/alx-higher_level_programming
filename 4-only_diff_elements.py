#!/usr/bin/python3

"different elements"

def only_diff_elements(set_1, set_2):
    same = {i for i in set_1 if i in set_2}
    different = set(i for i in (set_1.union(set_2)) if  i  not in same)
    return different
