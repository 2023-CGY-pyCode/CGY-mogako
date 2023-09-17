import heapq
# from collections import deque
import sys
input = sys.stdin.readline
print = sys.stdout.write

N, L = list(map(int, input().split()))

li = map(int, input().split())

h = list()
# heapq.push(h, dq.popleft())
for idx, i in enumerate(li):
    # print(h)
    if idx-L+1 <= 0:
        heapq.heappush(h, (i, idx)) # 인덱스랑 같이 묶어줌
        print(str(h[0][0]) + " ")
    elif idx-L+1 > 0: # 빼줘야함
        heapq.heappush(h, (i, idx)) #인덱스랑 같이 묶어줌
        while h[0][1] < idx-L+1:
            heapq.heappop(h)
            
        print(str(h[0][0]) + " ")
        
        
        
        
