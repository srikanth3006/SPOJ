n,x = map(int, raw_input().split())

s = map(int, raw_input().split())
q = map(int, raw_input().split())

result = list()
# import pdb;pdb.set_trace()
for i in range(len(s)):
    if s[i] == q[i]:
        result.append(i+1)
    else:
        for k in range(-x,x+1):
            if (i+k+1 < len(q)) and (i+k >= 0):
                if s[i] == q[i+k]:
                    result.append(i+1)
                    continue

print ' '.join(map(str, result))