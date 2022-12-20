#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    lst = []
    if my_list == None:
        return
    for i in my_list:
        lst.insert(0, i)
    for h in lst:
        print("{:d}".format(h))
