import sys

n = int(sys.stdin.readline())
num_list = list(map(int, sys.stdin.readline().split()))
m = max(num_list)

edit_list = list(map(lambda x: x/m*100, num_list))
print(sum(edit_list) / n)