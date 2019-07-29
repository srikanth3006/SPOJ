t = int(raw_input())

for _ in range(t):
    s = int(raw_input())
    for i in range(s):
        char = ''
        for j in range(s):
            if i==0 or i==s-1:
                char += '*'
            elif i==1:
                if j==s-1:
                    char += '*'
                else:
                    char += '.'
            elif i == s-2:
                if j==0 or j==s-1:
                    char += '*'
                else:
                    char += '.'
            elif i%2 == 0:
                if j == s-i:
                    char += '.'
                else:
                    char += '*'
            else:
                if i%s == 0:
                    pass