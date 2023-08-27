import sys
input = sys.stdin.readline

N = int(input())

arr = []

for i in range(1, N+1):
    x,y,z = map(int, input().split())
    arr.append((i,x,y,z)) # 행성 번호, x,y,z
    
graphs = set()

for k in range(1, 4):
    arr.sort(key = lambda x:x[k]) # x기준으로 정렬, y기준으로 정렬, z기준으로 정렬
    for idx in range(len(arr)-1):
        p1, x1, y1, z1 = arr[idx]
        p2, x2, y2, z2 = arr[idx+1]
        
        value = min(abs(x1-x2), abs(y1-y2), abs(z1-z2))
        graphs.add((p1, p2, value))
        
graphs = list(sorted(graphs, key=lambda x:x[2]))  # value기준 오름차순 정렬

parents = [i for i in range(N+1)] # 자기자신을 부모로 가지는 배열

def find(node: int):
    if node == parents[node]:
        return node # 자기자신
    
    parents[node] = find(parents[node])
    return parents[node]

def union(A:int, B:int): # A < B 
    pa = find(A)
    pb = find(B)
    
    parents[pb] = pa # pb의 최상위 부모가 A의 최상위 부모가 됨


count = 0
weighted_value = 0
for item in graphs:
    if count == N - 1:
        break
    p1, p2, value = item
    
    if p1 > p2: # 작은거 정렬
        p1, p2 = p2, p1
        
    if find(p1) != find(p2): # 부모가 다르다
        union(p1, p2)
        weighted_value += value
        count += 1

print(weighted_value)
    
    
    