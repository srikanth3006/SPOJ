t = int(raw_input())

for _ in range(t):
    rows, columns, size = map(int, raw_input().split())
    output = ""
    char = ""
    # for _ in range(rows):
    for i in range(2*size*rows):
        output = ""
        for j in range(2*size*columns):
            if j >= 2*size:
                j = j%(2*size)
            if i >= 2*size:
                i = i%(2*size)
            if j == (size+i) or j == (i-size):
                char = '\\'
            elif j == (size-i-1) or j == (3*size-i-1):
                char = '/'
            else:
                char = '.'

            output = output+char
        print output

# t = int(raw_input())
#
# for _ in range(t):
#     rows, columns, size = map(int, raw_input().split())
#     output = ""
#     char = ""
#     for _ in range(rows):
#         for i in range(2 * size):
#             output = ""
#             for _ in range(columns):
#                 for j in range(2 * size):
#                     if j == (size + i) or j == i - size:
#                         char = '\\'
#                     elif j == (size - i - 1) or j == (3 * size - i - 1):
#                         char = '/'
#                     else:
#                         char = '.'
#                     output = output + char
#             print output