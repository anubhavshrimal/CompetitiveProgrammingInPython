

n = int(input())
times = []
for i in range(n):
    a, b, c = list(map(int, input().split()))
    times.append([a, b+c])

times.sort(key=lambda x: -x[1])


for i in range(1, n):
    times[i][0] += times[i-1][0]

min_time = -1
for t in times:
    min_time = max(min_time, t[0]+t[1])

print(min_time)
