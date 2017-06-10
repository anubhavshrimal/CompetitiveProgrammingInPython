

n = int(input())

seq = input().split()

depth = 0
start_index = 0
curr_seq = 0

# maximum depth value
max_depth = 0
# start index of max depth
depth_start = 0
# maximum sequence length
max_seq_len = 0
# start index of max sequence
max_seq_start = 0

for i, b in enumerate(seq, start=1):
    if b == '1':
        depth += 1
        if depth == 1:
            start_index = i
    elif b == '2':
        depth -= 1

    curr_seq += 1

    if max_depth < depth:
        max_depth = depth
        depth_start = i

    if depth == 0:
        if curr_seq > max_seq_len:
            max_seq_len = curr_seq
            max_seq_start = start_index
        curr_seq = 0

print(max_depth, depth_start, max_seq_len, max_seq_start)
