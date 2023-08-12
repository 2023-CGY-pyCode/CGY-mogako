import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def dfs(y, x):
    if y == N-1 and x == M-1:
        return 1
    if checked[y][x] != -1:
        return checked[y][x]
    
    checked[y][x] = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < M and 0 <= ny < N:
            if arr[y][x] > arr[ny][nx]:
                checked[y][x] = checked[y][x] + dfs(ny, nx)
                
    return checked[y][x]
# 삽입 
arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))
    
checked = [[-1] * M for _ in range(N)]
# checked[0][0] = 1




# [print(arr[i]) for i in range(len(arr))]

# print(bfs())
dfs(0, 0)
print(checked[0][0])
# print(checked[N-1][M-1])

# [print(checked[i]) for i in range(len(checked))]
    
    
    