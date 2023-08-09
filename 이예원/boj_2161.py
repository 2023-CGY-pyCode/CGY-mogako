import sys
from collections import deque

n = int(sys.stdin.readline())
cards = [i for i in range(1, n+1)]
q = deque(cards)

while q:
    p = q.popleft()
    print(p, end=' ')
    if len(q) != 0:
        last = q.popleft()
        q.append(last)