#!/usr/bin/python3
from sys import argv
c = 0
if __name__ == '__main__':
    for i in range(1, len(argv)):
        c += int(argv[i])
    print(c)
