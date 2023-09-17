import heapq
import sys
input = sys.stdin.readline
N = int(input())

pq = []
li = []
for _ in range(N):
    S, T = tuple(map(int, input().split()))
    li.append((S, T))
    

li.sort(key=lambda x:x[0])
hq = []

# heapq.heappush(hq, li[0][1]) # 강의가 끝나는 시간 저장

for S, T in li:
    if not hq:
        heapq.heappush(hq, T)
        continue
    if S < hq[0]: # 강의의 시작시간이 현재 강의의 끝나는시간보다 작을 경우
        heapq.heappush(hq, T) # 강의는 다른 강의실을 사용해야함
    else:
        heapq.heappop(hq) # 그 자리를 사용할 수 있음
        heapq.heappush(hq, T) # 끝나는 시간을 heapq에 저장, 
        
print(len(hq))
