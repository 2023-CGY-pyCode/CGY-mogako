import sys
import heapq
input = sys.stdin.readline

N, M = map(int, input().split())

pq = [[] for _ in range(N+1)] # 0번째 강의실은 안씀 

for i in range(M):
    k, s, e = map(int, input().split())
    if not pq[k]:
        heapq.heappush(pq[k], (s, e))
        print("YES")
        
    elif pq[k] and pq[k][0][1] <= s: # top에 있는 끝나는시간
        heapq.heappop(pq[k])
        heapq.heappush(pq[k], (s, e)) # 시작 시간 끝시간 넣음
        # print(pq[k][0], (s,e))
        print("YES")
    else:
        print("NO")

        
    
    
    
