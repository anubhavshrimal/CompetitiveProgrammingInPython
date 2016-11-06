import numpy as np

test = int(input())

for t in range(1, test+1):
    num = int(input())

    n1, n2 = abs(np.roots([1, 1, -(num-1)]))
    if int(n1) != n1 or int(n2)!= n2:
        ans = num-1
    else:
        if n1 == 1 or n1 == -1:
            ans = n2
        elif n2 == 1 or n2 == -1:
            ans = n1
        else:
            if n2 > n1:
                ans = n1
            else:
                ans = n2

    print('Case #'+str(t)+':',str(int(ans)))
