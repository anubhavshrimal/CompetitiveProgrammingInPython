import math

T = int(input())


r, xs, ys = 50, 50, 100
xc, yc = 50, 50

for t in range(1, T+1):
    p, xa, ya = list(map(int, input().split()))
    p *= 3.6

    k1 = r - math.sqrt((xa-xc)**2 + (ya-yc)**2)
    k2 = r
    if k1 < 0 or p == 0:
        color = 'white'
    elif k1 - k2 == 0:
        if p == 0:
            color = 'white'
        else:
            color = 'black'
    else:
        xp, yp = ((k1*xc) - (k2*xa))/(k1-k2), ((k1*yc) - (k2*ya))/(k1-k2)
        d = (xs - xp)**2 + (ys - yp)**2
        angle = math.acos(1 - (d/(2 * r**2)))
        angle = math.degrees(angle)
        if xa == 50:
            angle = 180
        elif xa < 50:
            angle = 360 - angle
        if angle <= p:
            color = 'black'
        else:
            color = 'white'

    print("Case #"+str(t)+":", color)
