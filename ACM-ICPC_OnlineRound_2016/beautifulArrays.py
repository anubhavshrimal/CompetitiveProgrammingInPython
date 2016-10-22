
test = int(input())

for t in range(test):
    n = int(input())
    op = len(list(filter(lambda x: x == 1 or x == 0, list(map(int, input().split())))))
    if op == n or op == n-1:
        print("yes")
    else:
        print("no")