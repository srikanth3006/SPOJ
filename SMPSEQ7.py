n = int(raw_input())
s = map(int, raw_input().split())

def seperate(n, s):
    i=0
    decrease=True
    while i < len(s)-1:
        if decrease:
            if s[i] > s[i+1]:
                pass
            else:
                decrease = False
        else:
            if s[i] < s[i+1]:
                decrease = False
            else:
                return False
        i = i + 1
    return True

if seperate(n, s):
    print 'Yes'
else:
    print 'No'