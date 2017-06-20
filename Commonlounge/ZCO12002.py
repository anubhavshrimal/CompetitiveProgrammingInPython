

def binary_search(time, arr, size):
    l = 0
    r = size - 1

    while l < r:
        mid = int((l+r)/2)
        if arr[mid] == time:
            return mid
        elif arr[mid] < time:
            l = mid + 1
        else:
            r = mid - 1
    return l


n, x, y = list(map(int, input().split()))

contests = []

for i in range(n):
    contests.append(list(map(int, input().split())))

v = list(map(int, input().split()))
w = list(map(int, input().split()))

v.sort()
w.sort()
min_time = float('inf')

for contest in contests:
    vtime = binary_search(contest[0], v, x)
    wtime = binary_search(contest[1], w, y)

    if v[vtime] > contest[0] and (vtime - 1) >= 0:
        vtime -= 1
    if w[wtime] < contest[1] and (wtime + 1) < y:
        wtime += 1
    if v[vtime] > contest[0] or w[wtime] < contest[1]:
        continue
    min_time = w[wtime] - v[vtime] + 1 if (w[wtime] - v[vtime] + 1) < min_time else min_time

print(min_time)
