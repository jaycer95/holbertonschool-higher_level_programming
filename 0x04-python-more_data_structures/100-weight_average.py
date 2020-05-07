#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list == []:
        return 0
    return sum(list((x * y) for x,y in my_list)) / sum(i[1] for i in my_list)
