import sys

n = int(sys.stdin.readline())
s_list = [sys.stdin.readline().rstrip() for _ in range(n)]
s_list.sort()

dict = {}
for s in s_list:
    if s in dict:
        dict[s] += 1
    else:
        dict[s] = 1

print(max(dict, key=lambda x: dict.get(x)))