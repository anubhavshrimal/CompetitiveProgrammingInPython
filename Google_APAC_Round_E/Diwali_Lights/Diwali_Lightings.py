

test = int(input())

dic = [0] * 101


def numOfB(pos, seq_size, totalB):
    return (int(pos/seq_size) * totalB) + dic[pos % seq_size]

for t in range(1, test+1):
    seq = list(input())

    inPos, outPos = list(map(int, input().split()))
    inPos -= 1
    
    seq_size = len(seq)
    seq = ['X'] + seq
    count = 0
    for j in range(1, seq_size+1):
        if seq[j] == 'B':
            count += 1
            dic[j] = dic[j-1]+1
        else:
            dic[j] = dic[j-1]

    a = numOfB(outPos, seq_size, count)
    b = numOfB(inPos, seq_size, count)

    print('Case #'+str(t)+':',str(a-b))


