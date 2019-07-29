def prime_generator(no_of_primes):
    primes = list()
    primes.append(2)
    primes.append(3)
    num = 5
    while len(primes) != no_of_primes:
        for i in range(2, int(num/2)+1):
            if num %i == 0:
                break
        else:
            primes.append(num)
        num = num+2
    return primes

for _ in range(int(raw_input())):
    sums = list()
    n = int(raw_input())
    primes = prime_generator(3*n)
    j = 0
    for i in range(len(primes)/3):
        sums.append(primes[j]*primes[j+1]+primes[j+2])
        j = j+3
    print ' '.join(map(str, sums))
