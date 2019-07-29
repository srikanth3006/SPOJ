# your code goes here
n = int(raw_input())
s = ''
for i in range(n):
    if i % 2 == 0:
        s += 'I hate'
    else:
        s += 'I love'
    if i != n-1:
        s += ' that '

print '%s it' % s