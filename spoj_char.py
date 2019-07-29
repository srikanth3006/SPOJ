t = int(raw_input())

for _ in range(t):
    rows, columns, square = map(int, raw_input().split())
    output = ""
    for i in range((square+1)*rows+1):
        for j in range((square+1)*columns+1):
            if i%(square+1)==0 or j%(square+1)==0:
                char = '*'
            elif (j+i)%2 == 0:
                if (i+j)%(square+1) == 0 and ((i+j)/(square+1))%2 == 0:
                    char = "/"
                elif (abs((i-j))%(square+1) == 0 and ((i-j)/(square+1))%2 == 0):
                    char = "\\"
                else:
                    char = '.'
            else:
                char = '.'

            output = output + char
        print output
        output = ""

