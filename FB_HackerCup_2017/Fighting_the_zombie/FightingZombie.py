

import re
from functools import reduce
from operator import mul
from fractions import Fraction


def C(n, k):
    return int(reduce(mul, (Fraction(n - i, i + 1) for i in range(k)), 1))


def notPossible(x, n, s):
    sum = 0

    for i in range(1, s+1):
        for z in range(0, int((i-n)/x)+1):
            sum += ((-1)**z * C(n, z) * C(i-x*z-1, n-1))
    return sum


T = int(input())

for t in range(1, T+1):
    D, S = list(map(int, input().split()))
    s = list(input().split())

    for i in range(len(s)):
        l = re.findall(r'\d+', s[i])
        H = D
        if len(l) == 3:
            n, x, z = list(map(int,l))
            if '+' in s[i]:
                H -= z
            else:
                H += z
        else:
            n, x = list(map(int,l))

        if H <= n:
            s[i] = 1
            continue
        elif H > n*x:
            s[i] = 0
            continue
        else:
            notPos = notPossible(x, n, H-1)
            total = x**n
            s[i] = (total - notPos)/total

    probability = max(s)
    probability = round(probability, 6)

    print("Case #"+str(t)+":","%.6f" % probability)
