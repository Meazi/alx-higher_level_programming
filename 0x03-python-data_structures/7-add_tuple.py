#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) < 2 or len(tuple_b) < 2:
        if len(tuple_a) == 0:
            tuple_a = (0, 0)
        else:
            tuple_a = tuple_a + (0,)
        if len(tuple_b) == 0:
            tuple_b = (0, 0)
        else:
            tuple_b = tuple_b + (0,)
    elif len(tuple_a) > 2 or len(tuple_b) > 2:
        itm1 = tuple_a[:2]
        itm2 = tuple_b[:2]
    a1 = tuple_a[0]
    a2 = tuple_a[1]
    b1 = tuple_b[0]
    b2 = tuple_b[1]
    return ((a1 + b1), (a2 + b2))
