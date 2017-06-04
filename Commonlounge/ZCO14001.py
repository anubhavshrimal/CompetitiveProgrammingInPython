

n, full = list(map(int, input().split()))

stacks = list(map(int, input().split()))

commands = list(input().split())

empty = left = 0
right = len(stacks) - 1

crane = 0
handEmpty = True

for c in commands:
    if c == '1':
        if crane != left:
            crane -= 1
    elif c == '2':
        if crane != right:
            crane += 1
    elif c == '3':
        if stacks[crane] != empty and handEmpty:
            stacks[crane] -= 1
            handEmpty = False
    elif c == '4':
        if stacks[crane] != full and not handEmpty:
            stacks[crane] += 1
            handEmpty = True
    else:
        break

for boxes in stacks:
    print(boxes, end=' ')
