#!/usr/bin/python3
""" Print a sorted list """


class MyList(list):
    """ class that inhetits from list """

    def print_sorted(self):
        print(sorted(self))
