#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if 97 <= ord(i) <= 122:
            a = ord(i) - 32
        else:
            a = ord(i)
        print("{:c}".format(a), end="")
    print("")
