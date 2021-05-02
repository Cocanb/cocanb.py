from numpy.random import choice
from re import findall, sub

def add_spaces(initial):
    special = findall(initial, "<.*>")
    replaced = sub(initial, "<.*>")
    for i in replaced:
        replaced[replaced.index(i)] = i + choice(["", " "], p=[0.6, 0.4]) #change
    final = sub(" +", " ")
    return final