#!/usr/bin/python3
# 4-list_division.py
# ezra.mallo@gmail.com


def list_division(my_list_1, my_list_2, list_length):
    """Function that divides element by element 2 lists."""

    new_list = []
    for i in range(0, list_length):
        try:
            result = my_list_1[i] / my_list_2[i]
        except TypeError:
            print("wrong type")
            result = 0
        except ZeroDivisionError:
            print("division by zero")
            result = 0
        except IndexError:
            print("out of range")
            result = 0
        finally:
            new_list.append(result)
    return (new_list)
