

n = int(input())    # number of friends
x = int(input())    # number of frames

combinations = (2**n) - 1

print(abs(combinations-x))