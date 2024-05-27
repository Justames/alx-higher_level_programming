#!/usr/bin/python3

"common elements"

def common_elements(set_1, set_2):
    common = {i for i in set_1 if i in set_2}
    return common
