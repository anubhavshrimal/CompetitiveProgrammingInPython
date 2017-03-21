

def appearanceCount(window, seqLen, pattern, sequence):
    pattern = ''.join(sorted(pattern))
    count = 0

    for i in range(seqLen - window):
        matcher = ''.join(sorted(sequence[i: i+window]))
        if pattern == matcher:
            count += 1
    return count


window = int(input())
seqLen = int(input())
pattern = input()
sequence = input()
print(appearanceCount(window, seqLen, pattern, sequence))
