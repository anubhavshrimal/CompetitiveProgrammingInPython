from math import ceil

T = int(input())

def find_cities_count(n, ts, tf, cities, c, count_c, time):
    if c == n:
        if time > tf:
            return -1
        else:
            return count_c
    elif time > tf:
        return -1
    else:
        x = ceil((time + ts - cities[c][0]) / cities[c][1])
        with_ts = find_cities_count(n, ts, tf, cities, c + 1, count_c + 1, cities[c][0] + x * cities[c][1] + cities[c][2])

        x = ceil((time - cities[c][0]) / cities[c][1])
        if x < 0:
            x = 0
        without_ts = find_cities_count(n, ts, tf, cities, c + 1, count_c, cities[c][0] + x * cities[c][1] + cities[c][2])
        return max(with_ts, without_ts)


for t in range(1, T+1):
    n, ts, tf = list(map(int, input().split()))
    cities = []
    for i in range(n-1):
        cities.append(list(map(int, input().split())))

    a = find_cities_count(n-1, ts, tf, cities, 0, 0, 0)
    if a < 0:
        print("Case #{}: IMPOSSIBLE".format(t))
    else:
        print("Case #{}: {}".format(t, a))