t = int(raw_input())

def calculate_sum(num):
    total = 0
    while num > 0:
        rem = num%10
        total = total+rem
        num = num/10
    return total


for _ in range(t):
    num = int(raw_input())
    print calculate_sum(num)