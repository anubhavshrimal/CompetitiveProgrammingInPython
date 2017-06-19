

n = int(input())
rectangles = []

for t in range(n):
    x, y = list(map(int, input().split()))
    if x > y:
        rectangles.append(y)
    else:
        rectangles.append(x)


rectangles.sort()

k = 0

for i in rectangles:
    if i >= (k+1):
        k += 1

print(k)
