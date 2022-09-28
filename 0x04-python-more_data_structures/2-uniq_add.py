#!/usr/bin/python3
def uniq_add(my_list=[]):
    uniq_int = set(my_list)
    uniq_sum = 0
    for i in uniq_int:
        uniq_sum += i
    return uniq_sum
