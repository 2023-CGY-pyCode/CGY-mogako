import sys
from collections import deque

n = int(sys.stdin.readline())
s = deque()

for _ in range(n):
    s.append(int(sys.stdin.readline()))

h = 0
cnt = 0
for _ in range(len(s)):
    tmp = s.pop()
    if tmp > h:
        h = tmp
        cnt+=1

print(cnt)