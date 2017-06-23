# function to find prime numbers less than or equal to num
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
    sum_primes = 0
    prime_set = set({})

    for i in range(2, len(intList)):
        if intList[i]:
            if i in prime_set:
                lis.append(i)
            sum_primes += i
            prime_set.add(sum_primes)

    return len(lis)


n = int(input())
primes = find_primes_sieve(n)
print(primes)
