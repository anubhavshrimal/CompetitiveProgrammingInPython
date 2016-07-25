#!/bin/python3

import sys


n = int(input().strip())
for t in range(n):
    s = input().strip()
    cost = len(''.join(set(s)))
    print(cost)

