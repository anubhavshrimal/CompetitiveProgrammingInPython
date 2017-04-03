

T = int(input())
for t in range(T):
    dish1 = set(input().split())
    dish2 = input().split()
    count = 0

    for ingredient in dish2:
        if ingredient in dish1:
            count += 1
        if count == 2:
            break

    if count == 2:
        print('similar')
    else:
        print('dissimilar')

