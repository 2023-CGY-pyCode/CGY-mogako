import sys
from collections import deque

tc = int(sys.stdin.readline())
for _ in range(tc):
    n, m = map(int, sys.stdin.readline().split())
    q = deque()
    imp = list(map(int, sys.stdin.readline().split()))
    for i in range(n):
        q.append([imp[i], i])

    count = 0
    while q:
        cur = q.popleft()
        isMax = True
        for i in range(len(q)):
            if cur[0] < q[i][0]:
                q.append(cur)
                isMax = False
                break
            count += 1
            if cur[1] == m:
                print(count)


