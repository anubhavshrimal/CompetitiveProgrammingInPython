
n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))

sums = 0
res = 0
for i in range(n):
    sums += arr[i] * (i+1)
    res += sums * arr[i]
    res %= (1000000007)
print(res)