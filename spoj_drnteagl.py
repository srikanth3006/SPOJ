import math
t = int(raw_input())

for i in range(t):
    try:
        n = int(raw_input())
    except ValueError as e:
        n = int(raw_input())
    index=distance=0
    for j in range(n):
        try:
            x, y = map(int, raw_input().split())
        except ValueError as e:
            x, y = map(int, raw_input().split())
        if math.sqrt(x*x+y*y) > distance:
            distance = math.sqrt(x*x+y*y)
            index=j

    print "Case %s: %s" %(i+1, index+1)