from collections import defaultdict

T = int(input())
for t in range(T):
    n, Q = list(map(int, input().split()))
    arr = list(map(int, input().split()))

    sorted_arr = sorted(arr)
    indexes = defaultdict(list)

    for i in range(n):
        if arr[i] not in indexes:
            indexes[arr[i]] = [-1, -1]
        if sorted_arr[i] not in indexes:
            indexes[sorted_arr[i]] = [-1, -1]

        indexes[arr[i]][0] = i
        indexes[sorted_arr[i]][1] = i

    for q in range(Q):
        x = int(input())
        swaps = 0
        indx = indexes[x][0]

        need_large = 0
        need_small = 0
        safe_large = 0
        safe_small = 0

        low = 0
        high = n - 1

        while low <= high:
            mid = int(low + ((high - low) / 2))
            if arr[mid] == x:
                break

            elif arr[mid] < x:
                if indx < mid:
                    need_large += 1
                    high = mid - 1
                else:
                    safe_small += 1
                    low = mid + 1

            else:
                if indx > mid:
                    need_small += 1
                    low = mid + 1
                else:
                    safe_large += 1
                    high = mid - 1

        swaps += min(need_large, need_small)
        safe_small += swaps
        safe_large += swaps

        if need_large > need_small:
            need = need_large - need_small
            available = n - indexes[x][1] - 1 - safe_large

            if available >= need:
                swaps += need
            else:
                swaps = -1
        elif need_large < need_small:
            need = need_small - need_large
            available = indexes[x][1] - safe_small

            if available >= need:
                swaps += need
            else:
                swaps = -1

        print(swaps)

