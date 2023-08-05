import sys
sys.setrecursionlimit(10**6)

input = sys.stdin.readline

n, m = tuple(map(int, input().split()))

p = [i for i in range(n+1)] # 자기 자신을 부모로

def find(node):
    if node == p[node]: # 현재 노드가 가bp지고 잇는 부모값이 현재 노드값이라면 일치
        return node
    
    p[node] = find(p[node]) # 현재 노드가 가지고 있는 부모값이 노드값이 아니라면 
    return p[node] # 현재 노드가 가지고있는 최상위 부모값을 리턴

def union(a, b): # a < b 
    pa = find(a)
    pb = find(b)
    p[pb] = pa  
    
    
for _ in range(m):
    oper, a, b = tuple(map(int, input().split()))
    
    if a > b:
        temp = a
        a = b
        b = temp
    if oper == 0:
        union(a, b)        
    else:
        if find(a) == find(b):
            print("YES")
        else:
            print("NO")
            
    print(p)
    
    
