#!/usr/bin/python3

""" Find list peak """


def find_peak(list_of_integers):
    """ Find peak function"""
    if list_of_integers is None or list_of_integers == []:
        return None
    length = len(list_of_integers)
    begin = 0
    end = length - 1
    while begin <= end:
        if begin == end:
            return list_of_integers[begin]
        middle = begin + (end - begin) // 2
        if list_of_integers[middle] < list_of_integers[middle + 1]:
            begin = middle + 1
        else:
            end = middle

    return None
