#!/usr/bin/python3

"ascending last"

def max_integer(my_list=[]):
    if not my_list:
        return none
    else:
        max_int = my_list[0]
        for i in my_list:
            if i > max_int:
                max_int = i
        return max_int
