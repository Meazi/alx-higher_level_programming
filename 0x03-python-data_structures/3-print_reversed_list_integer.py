#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    lst = []
    for i in my_list:
        lst.insert(0, i)
    for h in lst:
        print("{:d}".format(h))
