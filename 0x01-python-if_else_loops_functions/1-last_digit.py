#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    number_pos = number * (-1)
    last_num_pos = number_pos % 10
    last_digit = last_num_pos * (-1)
else:
    last_digit = number % 10
if last_digit > 5:
    print(f'Last digit of {number:d} is {last_digit:d} and is greater than 5')
elif last_digit == 0:
    print(f'Last digit of {number:d} is {last_digit:d} and is zero')
elif last_digit < 6 or last_digit != 0:
    print(f'Last digit of {number:d} is {last_digit:d}\
 and is less than 6 and not 0')
