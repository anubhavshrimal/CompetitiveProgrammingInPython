

n = int(input())

l = 6
inc = 16
v = 0
for i in range(1, n + 1):
    for k in range(n - i, 0, -1):
        print(' ', end='')
    for j in range(1, i + 1):
        v += l
        l += inc
        print("{0:05d}".format(v), end=' ')
    print()
