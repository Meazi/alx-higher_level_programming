#!/usr/bin/python3
def max_integer(my_list=[]):
    largest_num = None
    if my_list is None:
        return ("None")
    else:
        for num in my_list:
            if largest_num is None or largest_num < num:
                largest_num = num
        return (largest_num)
