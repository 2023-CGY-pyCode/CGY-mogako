import sys

n_list = list(map(int, sys.stdin.readline().split()))
n_list.sort()
for n in n_list:
    print(n, end=' ')