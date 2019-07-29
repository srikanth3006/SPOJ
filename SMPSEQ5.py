def main():
    n = int(raw_input().strip())
    num = raw_input().split(" ")
    num = [int(i) for i in num if i != '']
    m = int(raw_input().strip())
    mem = raw_input().split(" ")
    mem = [int(j) for j in mem if j!= '']
    result = list()
    i = 0
    for ele in num:
        if not i>=len(mem):
            if ele == mem[i]:
                result.append(i + 1)
            i += 1

    print ' '.join(map(str, result))
    return 0


if __name__ == "__main__":
    main()