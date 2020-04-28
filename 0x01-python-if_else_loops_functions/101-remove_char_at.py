#!/usr/bin/python3
def remove_char_at(str, n):
    str1 = ""
    i = 0
    for j in str:
        if i != n:
                str1 += j
        i += 1
    return str1
