t = int(raw_input())

for _ in range(t):
    rows, columns, h, w = map(int, raw_input().split())
    output = ""
    char = ""
    for i in range((rows + 1) * (h + 1) - 1):
        for j in range((columns+1)*(w+1)-1):
            if (i+1)%(h+1)==0 and (j+1)%(w+1) ==0:
                char = '+'
            elif (j+1)%(w+1) == 0:
                char = '|'
            elif (i+1)%(h+1)==0:
                char = '-'
            else:
                char = '.'
            output = output+char
        print output
        output = ""

    print output
