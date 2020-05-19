#!/usr/bin/python3
""" writing a class node """
class Node:
    """ defines a node of a singly linked list """


    def __init__(self, data, next_node=None):
        self.__data = data
        self.__next_node = next_node
    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError('data must be an integer')
        else:
            self.__data = value
    @property
    def next_node(self):
        return self.__nextnode

    @next_node.setter
    def next_node(self, value):
        if next_node is not None or not isinstance(next_node, Node):
            raise TypeError('next_node must be a Node object')
        else:
            self.__next_node = value

class SinglyLinkedList:
    """ defines a singly linked list """


    def __init__(self):
        self.__head = None

    
