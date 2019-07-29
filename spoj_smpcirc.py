import math
t = int(raw_input())

for _ in range(t):
    x1, y1, r1, x2, y2, r2 = map(int, raw_input().split())
    distance = math.sqrt(abs(x1-x2)*abs(x1-x2) + abs(y1-y2)*abs(y1-y2))
    if r2 == r1+distance or r1 == r2+distance:
        print 'E'
    elif r2 > r1+distance or r1 > r2+distance:
        print 'I'
    else:
        print 'O'