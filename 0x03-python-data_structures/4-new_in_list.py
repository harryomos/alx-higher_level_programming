#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx < 0:
        return my_list
    elif idx >= len(my_list):
        return my_list
    new_list = my_list.copy()
    for i, val in enumerate(new_list):
        if i == idx:
            new_list[i] = element
            return new_list
