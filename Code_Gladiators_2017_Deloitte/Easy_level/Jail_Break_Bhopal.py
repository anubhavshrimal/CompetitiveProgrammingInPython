def GetJumpCount(x, y, walls):
    z = x - y
    count = 0
    for wall in walls:
        while wall > x:
            wall -= z
            count += 1
        count += 1

    return count


x = int(input())
y = int(input())
n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))

print(GetJumpCount(x, y, arr))