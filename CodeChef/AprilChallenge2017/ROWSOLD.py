T = int(input())

for t in range(T):
    soldiers = input()
    row = len(soldiers)
    consecutive_sold = 0
    consecutive_cells = 0
    total_secs = 0
    i = 0
    while i < row and soldiers[i] != '1':
        i += 1

    if i != row:
        while i < row:
            consecutive_cells = 0
            while i < row and soldiers[i] == '1':
                consecutive_sold += 1
                i += 1
            while i < row and soldiers[i] == '0':
                consecutive_cells += 1
                i += 1
            if consecutive_cells > 0:
                consecutive_cells += 1
            total_secs += consecutive_cells * consecutive_sold

    print(total_secs)
