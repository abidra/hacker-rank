#!/bin/python3

import sys

def simpleArraySum(n, ar):
    # Complete this function
    sum_arrays = sum(ar)
    return sum_arrays

n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = simpleArraySum(n, ar)
print(result)
