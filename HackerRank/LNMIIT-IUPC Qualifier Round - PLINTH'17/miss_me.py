import re
from math import sqrt; from itertools import count, islice


def isPrime(n):
    return n > 1 and all(n%i for i in islice(count(2), int(sqrt(n)-1)))

T = int(input())
setPrime = set()

for t in range(0,T):
    primes = 0
    maxVal = 0
    string = input()
    string = re.findall(r'\d+', string)

    for i in range(len(string)):
        num = int(string[i])
        if num in setPrime or isPrime(num):
            setPrime.add(num)
            primes += 1
            if num > maxVal:
                maxVal = num

    print(primes, maxVal)