#!/bin/python3

import sys
import math

def encryption(s):
    root = math.sqrt(len(s))
    col, row = math.ceil(root), math.floor(root)
    if col * row < len(s):
        row += 1
    enc_s = []
    for i in range(col):        
        for j in range(row):
            if (i + col * j) < len(s):
                enc_s.append(s[i + col * j])            
            else:
                break
        enc_s.append(' ')       
    return ''.join(enc_s)

if __name__ == "__main__":
    s = input().strip()
    result = encryption(s)
    print(result)
