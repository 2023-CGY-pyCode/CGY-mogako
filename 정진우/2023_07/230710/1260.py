import sys
from collections import deque
N, M, V = tuple(map(int, input().split()))

arr = [[] * (N+1) for _ in range(N+1)]
visited = [0] * (N+1)
for _ in range(M):
    v, e = tuple(map(int, input().split()))
    arr[v].append(e)
    arr[e].append(v)
    
for i in range(N+1):
    arr[i].sort()

def DFS(e):
    if visited[e]:
        return
    else:
        visited[e] = 1
        print(e, end=" ")
        for i in arr[e]:
            DFS(i)
            
        
    
def BFS(e):
    dq = deque()
    if not visited[e]:
        dq.append(e)
        visited[e] = 1
    while(dq):
        edge = dq.popleft()
        print(edge, end=' ')
        for i in arr[edge]:
            if visited[i]:
                continue
            dq.append(i)
            visited[i] = 1


DFS(V)
# for i in range(1, len(arr)):
#     DFS(i)
print()
visited = [0] * (N+1)
BFS(V)
# for i in range(1, len(arr)):
#     BFS(i)
    