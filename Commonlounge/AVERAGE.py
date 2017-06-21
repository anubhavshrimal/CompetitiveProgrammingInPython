

n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))

arr.sort()

count = 0

for e in range(n):
    i = 0
    j = n - 1
    while i < j:
        if arr[i] + arr[j] == 2 * arr[e]:
            count += 1
            j -= 1
        elif arr[i] + arr[j] < 2 * arr[e]:
            i += 1
        else:
            j -= 1
print(count)