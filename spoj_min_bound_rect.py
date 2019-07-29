t = int(raw_input())

for _ in range(t):
    n = int(raw_input())
    rx1 = 1000
    ry1 = 1000
    rx2 = -1000
    ry2 = -1000
    for _ in range(n):
        objects = raw_input().split()
        if objects[0] == 'p':
            coordinates = map(int, objects[1:3])
            x1, y1, x2, y2 = (coordinates[0], coordinates[1], coordinates[0],coordinates[1])
        elif objects[0] == 'c':
            radius = int(objects[-1])
            cx, cy = map(int, objects[1:3])
            x1, y1, x2, y2 = (cx-radius, cx-radius, cy+radius, cy+radius)
        elif objects[0] == 'l':
            x1, y1, x2, y2 = map(int, objects[1:])

        if x1 < rx1:
            rx1 = x1
        if y1 < ry1:
            ry1 = y1
        if x2 > rx2:
            rx2 = x2
        if y2 > ry2:
            ry2 = y2
    print rx1,ry1,rx2,ry2



