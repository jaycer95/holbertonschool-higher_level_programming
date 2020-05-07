#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) is not str or roman_string is None:
        return 0
    fin = 0
    dicsimple = {'I': 1, 'V': 5, 'X': 10,
                 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    for i in range(len(roman_string)):
        if i + 1 < len(roman_string):
            a = roman_string[i]
            b = roman_string[i + 1]
            if dicsimple[a] >= dicsimple[b]:
                fin += dicsimple[a]
            else:
                fin -= dicsimple[a]
    fin += dicsimple[roman_string[-1]]
    return fin
