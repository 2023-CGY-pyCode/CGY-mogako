import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int ,input().split())

arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))
    
K = int(input())

farm_list = []

def edge_search():
    edge_y = [0, N-1]
    edge_x = [0, M-1]
    
    max_value = 0
    max_value_idx = (0, 0)
    
    for y in edge_y:
        for x in range(M):
            if arr[y][x] > max_value:
                max_value = arr[y][x]
                max_value_idx = (y, x)
                
    for x in edge_x:
        for y in range(N):
            if arr[y][x] > max_value:
                max_value = arr[y][x]
                max_value_idx = (y, x)
                
    return max_value_idx


y, x = edge_search()
arr[y][x] = 0

farm_list.append((y, x))

count = 1

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


def bfs(y, x, max_value, max_value_idx):
    dq = deque()
    dq.append((y, x))
    while dq:
        y, x = dq.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= ny < N and 0 <= nx < M:
                if arr[ny][nx] > max_value:
                    max_value_idx = (ny, nx)
    
    return max_value_idx
                    
    
while count != K:
    max_value_idx = edge_search()
    for y, x in farm_list:
        max_value = arr[max_value_idx[0]][max_value_idx[1]]
        max_value_idx = bfs(y, x, max_value, max_value_idx)
    
    ny, nx = max_value_idx
    arr[ny][nx] = 0
    farm_list.append(max_value_idx)
    count += 1
    
for y,x in farm_list:
    print(y+1, x+1)

                
            
           

