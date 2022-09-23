#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) == 0:
        x1, y1 = 0, 0
    elif len(tuple_a) < 2:
        x1, y1 = tuple_a[0], 0
    else:
        x1, y1 = tuple_a[0], tuple_a[1]
    if len(tuple_b) == 0:
        x2, y2 = 0, 0
    elif len(tuple_b) < 2:
        x2, y2 = tuple_b[0], 0
    else:
        x2, y2 = tuple_b[0], tuple_b[1]
    return x1 + x2, y1 + y2
