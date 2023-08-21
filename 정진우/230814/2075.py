import heapq
import sys
input = sys.stdin.readline

N = int(input())

min_pq = []
for i in range(N):
    for j in sorted(map(int, input().split())):
        if len(min_pq) <= N-1:
            heapq.heappush(min_pq, j)
        else:
            heapq.heappop(min_pq)
            heapq.heappush(min_pq, j)
    # print(min_pq)
print(min_pq[0])

# print(min_pq)