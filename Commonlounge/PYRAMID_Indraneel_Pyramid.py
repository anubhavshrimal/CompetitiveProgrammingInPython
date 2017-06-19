

n = int(input())
rectangles = []

for t in range(n):
    x, y = list(map(int, input().split()))
    if x > y:
        x, y = y, x
    rectangles.append([x, y])

rectangles.sort(key=lambda k: k[0])

k = 0

for i in rectangles:
    if i[0] >= (k+1):
        k += 1

print(k)
