t = int(raw_input())

for _ in range(t):
    n, q = map(int, raw_input().split())
    N = map(int, raw_input().split())
    B = map(int, raw_input().split())
    d = dict()
    low = N[0]
    d[0] = low

    if n != 1:
        for i in range(1, n):
            if low > N[i]:
                d[i] = N[i]
                low = N[i]
            else:
                d[i] = low
    for b in B:
        if d:
            print d[b - 1]
        else:
            print low