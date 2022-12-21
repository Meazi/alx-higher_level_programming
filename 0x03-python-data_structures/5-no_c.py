#!/usr/bin/python3
def no_c(my_string):
    new_string = ""
    for ch in my_string:
        if ord(ch) == 67 or ord(ch) == 99:
            continue
        else:
            # print(ch) 
            new_string = new_string + ch
    return(new_string)
