

string = list(input())
sets = set({})
count = 1
for i in range(len(string)):
    if i > 0 and string[i] == string[i-1]:
        count += 1
    else:
        count = 1
    sets.add((ord(string[i]) % 96) * count)

n = int(input())

for i in range(n):
    num = int(input())

    if num in sets:
        print("Yes")
    else:
        print("No")
