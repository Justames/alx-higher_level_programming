#!/usr/bin/python3
"function that retrieves an element"

def element_at(my_list, idx):
    if idx < 0 or idx >= len(my_list):
        return none
    else:
        return my_list[idx]
