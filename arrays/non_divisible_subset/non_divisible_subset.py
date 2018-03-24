#!/bin/python3

import sys

def nonDivisibleSubset(k, arr):    
    counts = [0]*k
    for num in arr:
        counts[num % k] += 1
    count = 0
    if counts[0] > 0:
        count += 1
    if k % 2 == 0 and counts[k // 2] > 0:
        count += 1    
    for i in range(1, k // 2 + 1):        
        if i != k - i:                        
            count += max(counts[i], counts[k - i])        
    return count

if __name__ == "__main__":
    n, k = input().strip().split(' ')
    n, k = [int(n), int(k)]
    arr = list(map(int, input().strip().split(' ')))
    print(nonDivisibleSubset(k, arr))
