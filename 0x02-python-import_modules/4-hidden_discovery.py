#!/usr/bin/python3
import hidden_4
for i in range(len(dir(hidden_4))):
    if dir(hidden_4)[i][0] != "_":
        print(dir(hidden_4)[i])
