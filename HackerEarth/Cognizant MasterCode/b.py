n = int(input())
arr = list(map(int, input().split()))

mod = 10**10 + 11
summation = 0

for i, num in enumerate(arr, start=1):
    summation += bin(num).count("1")**i
    summation %= mod

print(summation)
