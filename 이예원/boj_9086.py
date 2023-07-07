import sys

def input():
    return sys.stdin.readline().rstrip()

n = int(input())
s_list = [input() for _ in range(n)]

for s in s_list:
    print(s[0]+s[-1])


