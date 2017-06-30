n = int(input())
arr = list(map(int, input().split()))

moves = 0
for i in range(n-1):
    if arr[i] >= arr[i+1]:
        inc = arr[i] - arr[i+1] + 1
        arr[i+1] += inc
        moves += inc
print(moves)