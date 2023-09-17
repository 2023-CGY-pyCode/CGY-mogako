import sys
import heapq
input = sys.stdin.readline

N,M,X = map(int, input().split())

INF = int(1e9)
graph = [[] for _ in range(N+1)] # 0번은 안씀
# visited = [False] * (N+1) # 방문처리
distance = [[INF] * (N+1) for _ in range(N+1)]


# def get_smallest_node(node):
#     min_value = INF
#     idx = 0
#     for i in range(1, N+1):
#         if not visited[i] and distance[node][i] < min_value:
#             min_value = distance[node][i]
#             idx = i
#     return idx

# print(distance) (특정 -> 특정)
for _ in range(M):
    a,b,c = map(int, input().split())
    graph[a].append((b,c)) # a->b, cost c

for a in range(1, N+1):
    pq = []
    visited = [False] * (N+1) # 방문처리 배열 초기화
    # visited[a] = True # 시작 노드 방문처리
    heapq.heappush(pq, (0, a)) # 거리와 정점을 노드에 넣기
    distance[a][a] = 0 # 자기자신은 0으로 초기화
    
    while pq:
        cur_dist, cur_node = tuple(map(abs, heapq.heappop(pq)))
        
        
        for node in graph[cur_node]: # a 에서 b로
            b = node[0]
            c = cur_dist + node[1]
            
            if c < distance[a][b]:
                distance[a][b] = c # 최단거리 계산
                heapq.heappush(pq, (c, b))
            
            

# [[print(distance[i]) for i in range(N+1)]]
max_result = 0
for i in range(1, N+1):
    max_result = max(distance[i][X] + distance[X][i], max_result)

        
print(max_result)
    