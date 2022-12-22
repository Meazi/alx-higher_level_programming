#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for lst in matrix:
        for itm in range(0, len(lst)):
            if(itm < len(lst) - 1):
                print("{:d}".format(lst[itm]), end=" ")
            else:
                print("{:d}".format(lst[itm]), end="")
        print()
