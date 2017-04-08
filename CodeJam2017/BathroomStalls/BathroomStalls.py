import heapq

T = int(input())

for t in range(1, T+1):
    n, k = list(map(int, input().split()))

    heap = [-n]
    heapq.heapify(heap)
    x = y = float('inf')
    for i in range(k):
        n = -heapq.heappop(heap)
        if n % 2 == 0:
            x = int(n / 2) - 1
            heapq.heappush(heap, -(int(n / 2) - 1))
        else:
            x = int(n / 2)
            heapq.heappush(heap, -(int(n / 2)))
        y = int(n / 2)
        heapq.heappush(heap, -(int(n / 2)))

    print("Case #{}: {} {}".format(t, max(x, y), min(x, y)))
