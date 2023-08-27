N, M = map(int, input().split())

graph = [[] for _ in range(N+1)] # 0번쨰는 안쓰니까

for _ in range(M):
    li = list(map(int, input().split()))
    
    for idx in range(1, len(li)-1):
        graph[li[idx]].append(li[idx+1]) # li[idx] -> li[idx+1]
        
        
s = []
checked = [0] * (N+1)
finished = [0] * (N+1)

iscycle = False      

def dfs(node):
    if checked[node]:
        if finished[node] == 0 :
            print(0)
            exit()
        return # 이미 방문
    
    checked[node] = 1
    for vertex in graph[node]: # DFS
        dfs(vertex) # 
        
    s.append(node) # 마지막에 스택에 저장
    finished[node] = 1

for i in range(1, N+1):
    dfs(i)

print(*s[::-1])