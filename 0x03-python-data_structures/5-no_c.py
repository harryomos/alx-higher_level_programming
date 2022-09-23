#!/usr/bin/python3
def no_c(my_string):
    new_str = ""
    for x in my_string:
        if x == 'c' or x == 'C':
            continue
        else:
            new_str += x
    return new_str
