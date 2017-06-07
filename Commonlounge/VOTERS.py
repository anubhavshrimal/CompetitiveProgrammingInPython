

n1, n2, n3 = list(map(int, input().split()))
voters1 = []
voters2 = []
voters3 = []

for i in range(n1):
    voters1.append(int(input()))

for j in range(n2):
    voters2.append(int(input()))

for k in range(n3):
    voters3.append(int(input()))

final = []
remaining = []
i = j = k = 0

while i < n1 or j < n2 or k < n3:
    v1 = voters1[i] if i < n1 else float('inf')
    v2 = voters2[j] if j < n2 else float('inf')
    v3 = voters3[k] if k < n3 else float('inf')

    min_val = min(v1, v2, v3)
    count = 0
    if min_val == v1:
        count += 1
        i += 1
    if min_val == v2:
        count += 1
        j += 1
    if min_val == v3:
        count += 1
        k += 1

    if count >= 2:
        final.append(min_val)


print(len(final))

for voter in final:
    print(voter)

