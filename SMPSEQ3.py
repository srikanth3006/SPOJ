n = int(raw_input())
num = map(int, raw_input().split())
m = int(raw_input())
mem = map(int, raw_input().split())

result = list()
for i in num:
    for j in mem:
        if i==j:
            result.append(i)

print ' '.join(map(str, result))