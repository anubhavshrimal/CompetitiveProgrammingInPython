T = int(input())

for t in range(1, T+1):
    D, N = list(map(int, input().split()))
    max_time = -float('inf')
    for n in range(N):
        k, s = list(map(int, input().split()))
        max_time = max(max_time, (D - k)/s)
    speed = D / max_time
    print("Case #{}: ".format(t)+"{0:.6f}".format(speed))
