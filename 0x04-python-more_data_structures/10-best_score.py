#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    values = list(a_dictionary.values())
    sc = 0
    for j in values:
        if j > sc:
            sc = j
    for i in a_dictionary:
        if a_dictionary[i] == sc:
            return i
