#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence == "":
        return (len(sentence), None)
    else:
        x = len(sentence)
        y = sentence[0]
        return (x, y)
