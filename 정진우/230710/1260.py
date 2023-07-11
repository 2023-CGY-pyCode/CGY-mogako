import sys
from collections import deque
N, M, V = tuple(map(int, input().split()))

arr = [[0] * (N+1) for _ in range(N+1)]
for _ in range(M):
    v, e = tuple(map(int, sys.stdin.readline().split()))
    arr[v][e] = 1
    
# print(arr)
def DFS(V):
    for j in range(len(arr[V])):
        if arr[V][j] == 1:
            print(V, end=" ")
            DFS(j)

def BFS(V):
    d = deque()
    d.append(V)
    visited = [False] * (N+1)
    for i in range(N):
        while(d):
            vertex = d.popleft()
            if visited[vertex] == False:
                visited[vertex] = True
            elif visited[vertex] == True:
                continue
            print(vertex, end=" ")
            for i in range(len(arr[vertex])):
                if not visited[i] and arr[vertex][i]:
                    d.append(i)
        if not visited[i]:
            d.append(i)
                    
# DFS(V)
# print()
BFS(V)