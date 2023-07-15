import sys

n, l = map(int, sys.stdin.readline().split())
apple_list = list(map(int, sys.stdin.readline().split()))

apple_list.sort()
for apple in apple_list:
    if apple <= l:
        l += 1
    else:
        break

print(l)