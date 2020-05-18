#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        for length in range(x):
            print("{}".format(my_list[length]), end="")
            length += 1
        print()
        return length
    except IndexError:
        print()
        return length
