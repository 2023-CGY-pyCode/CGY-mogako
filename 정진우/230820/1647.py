import sys
input = sys.stdin.readline

N, M = map(int, input().split())

graph = []

ancestor = [i for i in range(N+1)]

for _ in range(M):
    A, B, C = map(int, input().split())
    graph.append((A, B, C))
    
graph.sort(key = lambda x:x[2]) # value기준 오름차순 정렬
# Union
def union(a, b):
    pa = find(a) # a의 부모 찾기
    pb = find(b) # b의 부모 찾기
    
    ancestor[pb] = pa # b의 부모를 pa로 연결 

# Find
def find(node): # node의 부모 찾기
    if node == ancestor[node]: # 만약 node가 부모의 노드와 같다며
        return node # node의 부모는 node 자기자신
    
    ancestor[node] = find(ancestor[node]) # 자기 자신 노드가 아니라면 부모의 노드로 다시 설정
    return ancestor[node] # 압축한 경로


count = 0
weighted = []
for item in graph: #mst 생성과정
    if count == len(ancestor)-1: # mst 완성
        break
    A, B, C = item
    
    if A > B: # 작은 정점이 앞으로
        A, B = B, A
        
    if find(A) != find(B): # not cycle
        union(A, B) # 같은 집합으로 두고
        weighted.append(C) # mst에 포함
        count += 1
        
print(sum(weighted[:-1]))