

def find_sum(a, b, n):
    summation = 0
    for i in range(n):
        summation += (a[i] * b[i])
    return summation

n, k = list(map(int, input().split()))
a = list(map(int, input().split()))
b = list(map(int, input().split()))

min_indx, min_val = min(enumerate(b), key=lambda x: x[1])
max_indx, max_val = max(enumerate(b), key=lambda x: x[1])
k *= 2

a[min_indx] += k
min_sum = find_sum(a, b, n)
a[min_indx] -= k

a[max_indx] -= k
max_sum = find_sum(a, b, n)
a[max_indx] += k

if min_sum < max_sum:
    print(min_sum)
else:
    print(max_sum)

