import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
stack = deque()
for _ in range(n):
    i = int(input())
    if i == 0:
        stack.pop()
    else:
        stack.append(i)

print(sum(stack))