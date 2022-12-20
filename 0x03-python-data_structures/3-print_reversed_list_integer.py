#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    l = []
    for i in my_list:
        l.insert(0, i)
    for h in l:
        print("{:d}".format(h))
