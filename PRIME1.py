import math

t = int(raw_input())


def is_prime(num):
    if num == 2:
        return True
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num))+1):
        if num%i == 0:
            return False
    return True


for _ in range(t):
    m,n = map(int, raw_input().split())
    result = list()
    for num in range(m,n+1):
        if is_prime(num):
            print num
    print '\n'
