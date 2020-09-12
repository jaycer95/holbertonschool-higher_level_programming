#!/usr/bin/python3

""" Find list peak """


def find_peak(list_of_integers):
	""" Find peak function"""
	if list_of_integers is None or list_of_integers == []:
        	return None
	length = len(list_of_integers)
	peak = list_of_integers[0]
	if length == 1:
		return peak
	if list_of_integers[length - 1] >= list_of_integers[length - 2]:
 		return list_of_integers[length - 1]
	for i in range(0, length - 1):
		if list_of_integers[i] >= list_of_integers[i + 1] and list_of_integers[i] >= list_of_integers[i - 1]:
			peak = list_of_integers[i]
	return peak 
