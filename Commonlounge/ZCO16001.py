import heapq

inputs = list(map(int, input().split()))

n, k = inputs[0], inputs[1]
shelf1 = inputs[2: 2+n]
shelf2 = inputs[2+n: 2+n+n]


def solve(arr1, arr2, k):
    minheap = []
    maxheap = []

    for x in arr1:
        minheap.append(x)
    for x in arr2:
        maxheap.append(-x)

    heapq.heapify(minheap)
    heapq.heapify(maxheap)

    while k > 0 and (minheap[0] < -maxheap[0]):
        k -= 1
        min_val = heapq.heappop(minheap)
        max_val = -heapq.heappop(maxheap)
        heapq.heappush(maxheap, -min_val)
        heapq.heappush(minheap, max_val)

    return -maxheap[0] + max(minheap)

print(min(solve(shelf1, shelf2, k), solve(shelf2, shelf1, k)))
