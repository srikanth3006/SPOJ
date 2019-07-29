t = int(raw_input())

for _ in range(t):
    n, x, y = map(int, raw_input().split())
    fac = x
    factors = list()
    while fac<n:
        if fac%x == 0 and fac%y != 0:
            factors.append(fac)
        fac = x+fac
    print ' '.join(map(str, factors))
