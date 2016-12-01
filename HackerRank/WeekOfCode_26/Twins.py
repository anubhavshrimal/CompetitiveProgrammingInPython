from math import sqrt

n,m = input().strip().split(' ')
n,m = [int(n),int(m)]

if n % 2 == 0:
    n += 1
if m % 2 == 0:
    m -= 1

def is_pair_twin(i,j):
    for k in range(3, int(sqrt(j))+1, 2):
        if i % k == 0 or j % k == 0:
            return False
    else:
        return True

count = 0
for i in range(n, m-1, 2):
    j = i + 2
    if is_pair_twin(i, j):
        count += 1

print(count)