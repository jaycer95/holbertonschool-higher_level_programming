#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    new_lis = []
    for i in my_list:
        if i % 2 == 0:
            new_lis.append(True)
        else:
            new_lis.append(False)
    return new_lis
