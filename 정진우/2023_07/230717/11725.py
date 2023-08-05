import sys
from collections import deque
input = sys.stdin.readline

N = int(input())

visited = [0] * (N+1)
ancestor = [0] * (N+1)

arr = [[] for i in range(N+1)] 
# print(arr)
for _ in range(N-1):
    e, v = tuple(map(int, input().split()))
    arr[e].append(v)
    arr[v].append(e)
    # print(arr)

# print(arr)
q = deque()    
q.append(1)
def bfs():    
    while q:
        node = q.popleft()
        # print(ancestor)
        # print(arr[node])
        if visited[node]:
            continue
        visited[node] = 1
        for i in arr[node]:
            if not visited[i]:
                q.append(i)
                ancestor[i] = node 
                    
bfs()                    
for i in range(2, N+1):
    print(ancestor[i])
    
    
    
