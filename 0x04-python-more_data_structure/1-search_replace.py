#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = [elem if search != elem else replace for elem in my_list]
    return new_list
