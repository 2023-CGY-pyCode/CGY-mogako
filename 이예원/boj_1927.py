import sys
import heapq
n = int(sys.stdin.readline())

hq = []
for _ in range(n):
    x = int(sys.stdin.readline())
    if x == 0:
        if len(hq) == 0:
            print(0)
        else:
            print(heapq.heappop(hq))
    else:
        heapq.heappush(hq, x)