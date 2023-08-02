import sys
from collections import deque

k = int(sys.stdin.readline())
s = deque()

for _ in range(k):
    n = int(sys.stdin.readline())

    if n==0:
        s.pop()
    else:
        s.append(n)

ans = 0
for i in range(len(s)):
    ans += s.pop()

print(ans)

