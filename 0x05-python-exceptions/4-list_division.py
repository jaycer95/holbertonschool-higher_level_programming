#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    mylist = []
    x = 0
    for i in range(list_length):
        try:
            x = (my_list_1[i] / my_list_2[i])
        except TypeError:
            print("wrong type")
            mylist.append(0)
        except ZeroDivisionError:
            print("division by 0")
            mylist.append(0)
        except IndexError:
            print("out of range")
            mylist.append(0)
        finally:
            mylist.append(x)
    return mylist
