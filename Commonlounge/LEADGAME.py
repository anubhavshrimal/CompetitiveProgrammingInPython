

n = int(input())
maximum, player = -float('inf'), 1

for i in range(n):
    p1, p2 = list(map(int, input().split()))
    lead = abs(p1 - p2)

    if lead > maximum:
        maximum = lead
        player = 1 if p1 > p2 else 2

print(player, maximum)

"""
Test case:
5
140 82
89 134
90 110
112 106
88 90

Expected Output:
1 58
"""