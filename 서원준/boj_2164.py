import sys
from collections import deque

n = int(sys.stdin.readline())

q = deque(i+1 for i in range((n)))

while len(q) != 1:
    q.popleft()
    q.append(q.popleft())

print(q[0])
