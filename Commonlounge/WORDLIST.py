

n = int(input())
words = set([])
for i in range(n):
    string = list(input().lower())
    for j in range(len(string)):
        if string[j] != ' ' and (ord('a') > ord(string[j])  or ord(string[j]) > ord('z')):
            string[j] = ' '
    for x in ''.join(string).split():
        words.add(x)

words = list(words)
words.sort()

print(len(words))
for word in words:
    print(word)


