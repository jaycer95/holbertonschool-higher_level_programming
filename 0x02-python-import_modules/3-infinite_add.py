#!/usr/bin/python3
from sys import argv
c = 0
for i in range(1, len(argv)):
    c += int(argv[i])
print(c)
