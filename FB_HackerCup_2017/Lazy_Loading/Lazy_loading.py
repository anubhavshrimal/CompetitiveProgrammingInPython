from collections import deque

T = int(input())

for t in range(1, T+1):
    N = int(input())
    obj = []
    for n in range(N):
        obj.append(int(input()))

    dq = deque(sorted(obj))
    turns = 0

    while len(dq) != 0:
        maxItem = dq.pop()
        val = 1
        while val * maxItem < 50 and len(dq) != 0:
            dq.popleft()
            val += 1

        if val * maxItem >= 50:
            turns += 1

    print("Case #"+str(t)+":", turns)
