import sys
from collections import deque

t = int(sys.stdin.readline())

for _ in range(t):
    n, m = map(int, input().split()) # n=개수, m=중요도
    q = deque(map(int, input().split()))
    q2 = deque(range(n))

    cnt=0
    while True:
        if q[0]==max(q):
            cnt +=1
            q.popleft()
            if q2.popleft() == m:
                print(cnt)
                break
        else:
            q.append(q.popleft())
            q2.append(q2.popleft())
