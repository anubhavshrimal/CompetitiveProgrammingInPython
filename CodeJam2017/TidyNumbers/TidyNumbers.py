

T = int(input())

for t in range(1, T+1):
    n = int(input())
    n = list(map(int, str(n)))

    pointer = len(n)
    for i in range(len(n) - 2, -1, -1):
        if n[i] > n[i+1]:
            n[i] -= 1
            pointer = i + 1

    if pointer < len(n):
        for i in range(pointer, len(n)):
            n[i] = 9

    n.reverse()
    while n and n[-1] == 0:
        n.pop()
    n.reverse()

    print("Case #{}: {}".format(t, ''.join(map(str, n))))

