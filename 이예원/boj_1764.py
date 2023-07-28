import sys

s_d = {}
n, m = map(int, sys.stdin.readline().split())
for _ in range(n):
    s_d[sys.stdin.readline().rstrip()] = 1

count_name = []
for _ in range(m):
    h = input()
    if h in s_d.keys():
        count_name.append(h)

count_name.sort()
print(len(count_name))
for name in count_name:
    print(name)