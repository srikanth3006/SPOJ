t = int(raw_input())
for _ in range(t):
    m, n, ci, cj = map(int, raw_input().split())
    for i in range(m):
        char = ""
        for j in range(n):
            if j == (cj-1)-abs(i-(ci-1)) or j == (cj-1)+abs(i-(ci-1)):
                char += '*'
            else:
                char += '.'
        print char