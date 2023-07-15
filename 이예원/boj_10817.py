import sys

n_list = list(map(int, sys.stdin.readline().split()))
n_list.sort()
print(n_list[1])