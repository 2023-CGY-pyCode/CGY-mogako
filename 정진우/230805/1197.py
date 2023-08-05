import sys
sys.setrecursionlimit(10**6)

input = sys.stdin.readline

V, E = map(int, input().split())

p = [i for i in range(V+1)]

li = []

for _ in range(E):
    A,B,C = map(int, input().split())
    
    li.append((A, B, C))

li.sort(key=lambda x:x[2]) # value기준 오름차순 정렬


def find(node):
    if node == p[node]: # 최상위 노드인경우
        return node
    
    p[node] = find(p[node]) # path compression
    return p[node] # 압축한 경로

def union(a, b):
    pa = find(a)
    pb = find(b)
    p[pb] = pa # 낮은순으로 정렬
    # pb = b의 최상위 부모 노드의 값
    # pa = a의 최상위 부모 노드의 값
    # p[pb] = pa
    # pb의 부모가 가지는 값을 pa로 바꿈
    # 즉, pa와 pb가 공통의 pa를 가짐으로써 둘이 연결
    
weighted_value = 0
count = 0

for item in li:
    if count == len(p)-1: # mst 완성
        continue 
    A, B, C = item
    
    if A > B: # 작은게 무조건 앞으로
        temp = A
        A = B
        B = temp
        
    if find(A) != find(B): # not cycle
        union(A, B)
        weighted_value += C
        count += 1
        
print(weighted_value)