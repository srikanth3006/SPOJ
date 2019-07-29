s = int(raw_input())
s_list = map(int, raw_input().split())
n = int(raw_input())
n_list = map(int, raw_input().split())


def sum_of_elements(arr):
    total = 0
    for ele in arr:
        total += ele
    return total


if sum_of_elements(s_list)/s > sum_of_elements(n_list)/n:
    print ' '.join(map(str, s_list))
else:
    print ' '.join(map(str, n_list))
