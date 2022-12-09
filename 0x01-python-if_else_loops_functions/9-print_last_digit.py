#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        number_pos = number * (-1)
        pos_mod = number_pos % 10
        print(pos_mod, end='')
        return(pos_mod)
    else:
        print(number % 10, end='')
