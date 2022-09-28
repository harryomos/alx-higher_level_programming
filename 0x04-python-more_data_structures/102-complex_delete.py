#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    if not a_dictionary or value not in a_dictionary.values():
        return a_dictionary
    keys = list(a_dictionary.keys())
    for val in keys:
        if value == a_dictionary.get(val):
            del a_dictionary[val]
    return a_dictionary
