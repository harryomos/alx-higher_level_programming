#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    else:
        my_dict = dict(my_list)
        sum_, div = 0, 0
        for x, y in my_dict.items():
            sum_ += x * y
            div += y
        return sum_/div
