
test = int(input())

while test > 0:
    test -=1
    stones = int(input()) - 1
    a = int(input())
    b = int(input())
    smaller = min(a, b)
    larger = max(a, b)
    difference = larger - smaller
    min_sum = stones * smaller
    max_sum = stones * larger

    if smaller == larger:
        print(min_sum)
    else:
        while min_sum <= max_sum:
            print(min_sum, end=' ')
            min_sum += difference
        print()

