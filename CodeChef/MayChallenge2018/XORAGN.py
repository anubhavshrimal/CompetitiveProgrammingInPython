

T = int(input())
for t in range(T):
    n = int(input())
    a = list(map(int, input().split()))

    res = 0
    for num in a:
        res ^= (num * 2)

    print(res)
