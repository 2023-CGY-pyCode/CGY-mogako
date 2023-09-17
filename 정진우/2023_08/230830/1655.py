import sys
import heapq
from collections import deque
input = sys.stdin.readline

N = int(input())

max_pq = []
min_pq = []

for _ in range(N):
    num = int(input())
    
    if len(max_pq) == len(min_pq):
        heapq.heappush(max_pq, -num) # 같으면 왼쪽
    else:
        heapq.heappush(min_pq, num) # 다르면 오른쪽
        
        
    if min_pq and min_pq[0] < -max_pq[0]:
        max_value = heapq.heappop(max_pq)
        min_value = heapq.heappop(min_pq)

        heapq.heappush(max_pq, -min_value)
        heapq.heappush(min_pq, -max_value)
        
    print(-max_pq[0])
    
        
    
        
    
    

