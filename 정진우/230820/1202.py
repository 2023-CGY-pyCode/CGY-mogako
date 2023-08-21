import sys
import heapq
input = sys.stdin.readline

N, K = map(int, input().split())

jewelies = []
bags = []

for _ in range(N):
    M, V = tuple(map(int, input().split()))
    jewelies.append((M, V))
    
for _ in range(K):
    bags.append(int(input()))
    
    
jewelies.sort() # 가치가 큰 순서대로 정렬
bags.sort() # 크기가 낮은 순서대로 정렬

result = 0

tmp = []

for bag in bags:
    while jewelies and jewelies[0][0] <= bag: # 가방에 넣을 수 있으면
        heapq.heappush(tmp, -jewelies[0][1]) # 값 넣음 
        heapq.heappop(jewelies) # 값 제거
    if tmp:
        print(jewelies)
        result -= heapq.heappop(tmp) # 가방에 들어갈 수 있는 가장 큰 값 제거
        
print(result)

    