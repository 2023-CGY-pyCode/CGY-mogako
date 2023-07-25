import sys
from collections import deque

n = int(sys.stdin.readline())
stack = deque()
for _ in range(n):
    stack.append(int(sys.stdin.readline()))

max_h = stack.pop()
count = 1
while stack:
    cur_h = stack.pop()
    if cur_h > max_h:
        count += 1
        max_h = cur_h

print(count)
