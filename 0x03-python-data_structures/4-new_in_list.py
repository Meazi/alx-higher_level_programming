#!/usr/bin/python3
import copy
def new_in_list(my_list, idx, element):
    if my_list is None:
        return
    lst = []
    for ls in my_list:
        lst.append(ls)
    if idx <= len(lst) - 1 and idx >= 0:
        lst[idx] = element
        new_element = lst
        return(lst)
