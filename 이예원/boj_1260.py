import sys
from collections import deque
input = sys.stdin.readline

n, m, v = map(int, input().split())
e = [[] for _ in range(n+1)]
visited = [0] * (n+1)
for _ in range(m):
    v1, v2 = map(int, input().split())
    e[v1].append(v2)
    e[v2].append(v1)

for i in range(1, n+1):
    e[i].sort()

# dfs
search = deque()
search.append(v)
while search:
    cur_v = search.popleft()
    if visited[cur_v] != 1:
        print(cur_v, end=' ')
        visited[cur_v] = 1
        if len(e[cur_v]) != 0:
            for connect_v in reversed(e[cur_v]):
                search.appendleft(connect_v)
print()
# bfs
search.append(v)
visited = [0] * (n+1)
while search:
    cur_v = search.popleft()
    if visited[cur_v] != 1:
        print(cur_v, end=' ')
        visited[cur_v] = 1
        if len(e[cur_v]) != 0:
            for connect_v in e[cur_v]:
                search.append(connect_v)