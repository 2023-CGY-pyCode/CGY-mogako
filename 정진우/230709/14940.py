from collections import deque
import sys

n, m = tuple(map(int, input().split()))

arr = []
isVisited = [[0] * m for _ in range(n)]
d = deque()

def bfs():
    while(d):
        i,j,depth = d.popleft()
        
        if i < 0 or i >= n or j < 0 or j >= m:
            continue
        
        if isVisited[i][j]:
            continue
        else:
            isVisited[i][j] = 1
            # print(i, j)
            
        if arr[i][j] == 0:
            continue
        
        arr[i][j] = depth
        
        if i-1 >= 0: # 북
            d.append((i-1, j, depth+1))
        if j-1 >= 0: # 서
            d.append((i, j-1, depth+1))
        if i+1 <= m-1: # 남
            d.append((i+1, j, depth+1))
        if j+1 <= n-1: # 동
            d.append((i, j+1, depth+1))
        
        # print(d)
        
    
for i in range(n):
    li = list(map(int, sys.stdin.readline().split()))
    arr.append(li)
    

for i in range(n):
    for j in range(m):
        if arr[i][j] == 2:
            d.append((i, j, 0))
            bfs()
            break
        
for i in range(n):
    for j in range(m):
        if arr[i][j] == 1 and not isVisited[i][j]:
            print(-1, end=" ")
        else:
            print(arr[i][j], end=" ")
    print()
        