#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for lst in matrix:
        for itm in lst:
            print("{}".format(itm), end = " ")
        print("\n")
