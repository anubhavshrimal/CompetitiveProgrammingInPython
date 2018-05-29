
mod = 10**9 + 7
fib = [0] * 100000
fib[1] = 1

for k in range(2, 100000):
    fib[k] = (fib[k - 1] + fib[k - 2]) % mod

T = int(input())
for t in range(T):
    m, n = list(map(int, input().split()))
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    sum_a = sum(a) % mod
    sum_b = sum(b) % mod

    if n == 1:
        res = sum_a
    else:
        res = (a[0] * fib[n-2] * m + sum_b * fib[n-1]) % mod

    res = (res * m) % mod

    multiplier = n - 2

    if multiplier > 0:
        multiplier = fib[multiplier] % mod

        diff = (sum_a - a[0] * m) % mod
        res = (res + multiplier * diff * m) % mod

    print(res % mod)
