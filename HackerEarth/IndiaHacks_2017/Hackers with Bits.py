

n = input()
arr = input().split()
count = len(max(''.join(arr).split('0')))


def find_max(arr):
    return len(max(arr.split('0')))


for i in range(len(arr)):
    if arr[i] == '1':
        for j in range(len(arr)):
            if i == j: 
                continue
            if arr[j] == '0':
                arr[j], arr[i] = arr[i], arr[j]
                c = find_max(''.join(arr))
                if c > count:
                    count = c
                arr[j], arr[i] = arr[i], arr[j]


print(count)