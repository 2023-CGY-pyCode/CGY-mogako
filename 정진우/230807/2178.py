import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

board = []
for _ in range(N):
    board.append([int(i) for i in str(input().strip())])
        
visited = [[1] * M for _ in range(N)]

def bfs():
    dq = deque()
    dq.append((0, 0))
    # count = 
    while dq:
        y, x = dq.popleft()
        # print(y, x)
        # count += 1
        for i in range(4):
            ddx = x + dx[i]
            ddy = y + dy[i]
            if 0 <= ddx < M and 0 <= ddy < N:
                if board[ddy][ddx] == 1 and visited[ddy][ddx] == 1:
                    dq.append((ddy, ddx))
                    visited[ddy][ddx] = visited[y][x] + 1
        if y == N-1 and x == M-1:
            return visited[y][x]

print(bfs())
            
                
    