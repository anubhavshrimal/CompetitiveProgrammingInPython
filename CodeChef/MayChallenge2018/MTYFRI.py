

T = int(input())
for t in range(T):
    n, k = list(map(int, input().split()))
    a = list(map(int, input().split()))

    even_indx = []
    odd_indx = []
    for i, val in enumerate(a):
        if i % 2 == 0:
            even_indx.append(val)
        else:
            odd_indx.append(val)

    even_indx.sort()
    odd_indx.sort()

    sum_motu = sum(even_indx)
    sum_tomu = sum(odd_indx)

    if sum_tomu > sum_motu:
        print("YES")
    else:
        i = 0
        while sum_tomu <= sum_motu and i < k and i < int(n/2):
            sum_motu -= even_indx[-i - 1]
            sum_motu += odd_indx[i]

            sum_tomu -= odd_indx[i]
            sum_tomu += even_indx[-i - 1]

            i += 1

        if sum_tomu > sum_motu:
            print("YES")
        else:
            print("NO")
