

n, k = list(map(int, input().split()))
rq, cq = list(map(int, input().split()))

obstacles = set({})

for i in range(k):
    ro, co = list(map(int, input().split()))
    obstacles.add((ro, co))

for i in range(n+2):
    obstacles.add((i, 0))
    obstacles.add((0, i))
    obstacles.add((n+1, i))
    obstacles.add((i, n+1))

moves = 0

i = rq
j = cq

# travel up
while i <= n:
    if (i+1, j) not in obstacles:
        moves += 1
        i += 1
    else:
        break
i = rq

# travel down
while i >= 1:
    if (i-1, j) not in obstacles:
        moves += 1
        i -= 1
    else:
        break
i = rq

# travel right
while j <= n:
    if (i, j+1) not in obstacles:
        moves += 1
        j += 1
    else:
        break
j = cq

# travel left
while j >= 1:
    if (i, j-1) not in obstacles:
        moves += 1
        j -= 1
    else:
        break
j = cq

# travel N-E
while j <= n and i <= n:
    if (i+1, j+1) not in obstacles:
        moves += 1
        j += 1
        i += 1
    else:
        break
i = rq
j = cq

# travel S-E
while j <= n and i >= 1:
    if (i-1, j+1) not in obstacles:
        moves += 1
        j += 1
        i -= 1
    else:
        break
i = rq
j = cq

# travel S-W
while j >= 1 and i >= 1:
    if (i-1, j-1) not in obstacles:
        moves += 1
        j -= 1
        i -= 1
    else:
        break
i = rq
j = cq

# travel N-W
while j >= 1 and i <= n:
    if (i+1, j-1) not in obstacles:
        moves += 1
        j -= 1
        i += 1
    else:
        break

print(moves)