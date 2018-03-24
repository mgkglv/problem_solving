#!/bin/python3

import sys

def extraLongFactorials(n):   
    prev = [1]	
    res = []
    carry = 0
    for i in range(2, n + 1):
	for digit in prev:
	    prod = digit*i + carry
	    carry = prod % 10
	    res.append(prod // 10)
	while carry > 0:
	    res.append(carry % 10)
	    carry //= 10
	prev = res[:]
	res = []
    for digit in prev[::-1]:
	print(digit)


if __name__ == "__main__":
    n = int(input().strip())
    extraLongFactorials(n)
