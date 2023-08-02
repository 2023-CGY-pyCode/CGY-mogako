import sys
from collections import deque
input = sys.stdin.readline

N, M = tuple(map(int, input().split()))

dx = [1, 0, -1, 0] # 동남서북
dy = [0, -1, 0, 1]

visited = [[[False] * 2 for _ in range(M)] for _ in range(N)] # 방문배열

arr = []
for _ in range(N):
   li = [int(i) for i in input().strip()]
   arr.append(li)
   
   
def bfs():
    q = deque() # x, y, wall_count, count
    q.append((0, 0, 0, 1))
    while q:
        y, x, wall_count, count = q.popleft()
        if y == N-1 and x == M-1:
            return count
        for i in range(4):
            if x+dx[i] < 0 or x+dx[i] >= M or y+dy[i] < 0 or y+dy[i] >= N:
                continue
            else:
                if visited[y+dy[i]][x+dx[i]][wall_count] == 0:
                    if arr[y+dy[i]][x+dx[i]] == 1:
                        if wall_count == 0:
                            q.append((y+dy[i], x+dx[i], wall_count+1, count+1))
                            visited[y+dy[i]][x+dx[i]][1] = True
                        else:
                            continue
                    elif arr[y+dy[i]][x+dx[i]] == 0:
                        q.append((y+dy[i], x+dx[i], wall_count, count+1))
                        visited[y+dy[i]][x+dx[i]][wall_count] = True
    return -1


print(bfs())