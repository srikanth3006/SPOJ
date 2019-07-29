def convert(num):
    bin_num = 0
    a = 1
    while num > 0:
        rem = num%2
        bin_num = bin_num + rem*a
        num = num/2
        a = a*10
    return str(bin_num).rjust(8, '0')

def convert_to_int(bin_num):
    num = 0
    factor = 0
    while bin_num > 0:
        rem = bin_num %10
        num = num + pow(2, factor)*rem
        bin_num = bin_num/10
        factor += 1
    return num

t = int(raw_input())
for _ in range(t):
    hdpw = None
    n = raw_input()
    tups = raw_input().split()
    string = raw_input()
    passwd_bits = list()
    for tup in tups:
        ab = bb = 0
        ai = 0
        bi = 3
        a = 1
        bin_tuples = list()
        for char in tup:
            bin_tuples.append(convert(ord(char)))
        # print bin_tuples
        for bin_tup in bin_tuples:
            bi = (ai+3)%6
            if ai >= 6:
                ai = ai - len(bin_tup)
            if bi >= 6:
                bi = bi - len(bin_tup)

            ab = ab + int(bin_tup[-(ai+1)])*a
            bb = bb + int(bin_tup[-(bi+1)])*a
            ai+= 1
            a = a*10
        passwd_bits.append(convert_to_int(ab))
        passwd_bits.append(convert_to_int(bb))
    # print passwd_bits
    print ''.join(string[index] for index in passwd_bits)
    dummy = raw_input()
