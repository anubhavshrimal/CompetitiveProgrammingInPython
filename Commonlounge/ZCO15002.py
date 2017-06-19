

def binary_search(arr, val, l):
    global n
    r = n - 1

    while l <= r:
        mid = int((l + r) / 2)
        if arr[mid - 1] < val <= arr[mid]:
            return mid
        elif arr[mid] < val:
            l = mid + 1
        else:
            r = mid - 1
    return l


n, k = list(map(int, input().split()))
arr = list(map(int, input().split()))

arr.sort()
sets = 0
for i, val in enumerate(arr):
    index = binary_search(arr, val+k, i)
    sets += (n - index)

print(sets)
