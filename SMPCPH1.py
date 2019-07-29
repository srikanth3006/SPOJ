n = int(raw_input())
s = raw_input()
m = int(raw_input())
lines = list()

for _ in range(m):
    lines.append(raw_input())

for line in lines:
    for i in range(len(line)):
        char = line[i]
        if char in s:
            if s.index(char) == n-1:
                line = line[:i] + s[0] + line[i+1:]
            else:
                line = line[:i] + s[(s.index(char))+1] + line[i + 1:]
    print line