#!/bin/python3

import sys

def biggerIsGreater(s):    
    s = list(s)
    ln = len(s)
    index = ln - 1
    while s[index] <= s[index - 1] and index >= 1:
        index -= 1
    if index == 0:
        return 'no answer'
    min_index = ln - 1  
    while s[min_index] <= s[index - 1]:
        min_index -= 1
    s[min_index], s[index - 1] = s[index - 1], s[min_index]
    s[index:] = reversed(s[index:])

    return "".join(s)     


if __name__ == "__main__":
    T = int(input().strip())
    for a0 in range(T):
        w = input().strip()
        result = biggerIsGreater(w)
        print(result)
