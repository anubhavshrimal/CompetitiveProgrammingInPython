test = int(input())
for t in range(test):
    a = list(map(int, input().split()))
    if (a[0] == a[2] or a[1] == a[3]) and (a[0] != a[1] or a[2] != a[3]):
        if a[0] > a[2]:
            print("left")
        elif a[0] < a[2]:
            print("right")
        elif a[1] > a[3]:
            print("down")
        else:
            print("up")
    else:
        print("sad")