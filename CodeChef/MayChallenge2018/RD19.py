

# from math import gcd
def find_primes_sieve(num):
    # list of all numbers upto n
    intList = [True for i in range(num+1)]

    # first prime
    p = 2

    while p * p <= num:

        # if intList[p] is True means its a prime number
        if intList[p]:
            for i in range(p**2, num+1, p):
                intList[i] = False

        p += 1

    lis = []
    for i in range(2, len(intList)):
        if intList[i]:
            lis.append(i)

    return lis


primes = find_primes_sieve(49999)
T = int(input())
for t in range(T):
    n = int(input())

    numbers = list(map(int, input().split()))

    even_present = False
    odd_present = False
    one_present = False

    for num in numbers:
        if num % 2 == 0:
            even_present = True
            if odd_present:
                break
        elif num != 1:
            odd_present = True
            if even_present:
                break
        else:
            one_present = True
            break

    if one_present:
        print(0)
    elif even_present and not odd_present:
        print(-1)
    else:
        prime_divisible = True

        for prime in primes:
            j = 0
            prime_divisible = True

            while j < n:
                if numbers[j] % prime != 0:
                    prime_divisible = False
                    break
                j += 1

            if prime_divisible:
                break

        if prime_divisible:
            print(-1)
        else:
            print(0)
