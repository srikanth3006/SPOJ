t = int(raw_input())

for _ in range(t):
    n,m = map(int, raw_input().split())
    A = raw_input()
    B = raw_input()
    d = dict()
    for ch in B:
        d[ch] = 0
    for ele in d:
        for i in A:
            if i==ele:
                d[ele] += 1

    low = d.values()[0]
    for num in d.values():
        if num < low:
            low = num
    print low