import itertools

n, m = map(int, input().split())

a = []

for i in range(n):
    a.append(int(input(), 2))

maxCount = -1
maxTeam = 0

for i, j in itertools.combinations(range(n),2):
    count = bin(a[i] | a[j]).count('1')
    if count > maxCount:
        maxCount = count
        maxTeam = 1
    elif maxCount == count:
        maxTeam += 1

print(maxCount)
print(maxTeam)

