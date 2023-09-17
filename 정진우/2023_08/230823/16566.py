import sys
sys.setrecursionlimit(325000)
# sys.setrecursionlimit(4000000)
input = sys.stdin.readline
N, M, K = map(int, input().split())

blue = list(map(int, input().split()))
red = list(map(int, input().split()))

arr = [0] * (N+1)
p = [i+1 if i != N else 1e7 for i in range(N+1)] # 자기 자신보다 적어도 1은 크되, 마지막 값보다 큰 것은 없다.

for i in range(len(blue)): # blue card check
    arr[blue[i]] = 1
    
def union(A: int, B: int): # B > A always
    pb = find(B)
    
    p[A] = pb
    
def find(node):
    if p[node] >= 1e7:
        return node
    
    if arr[p[node]] == 1:
        return node
    
    p[node] = find(p[node])
    return p[node]
    
    
for red_card in red:
    m = p[red_card] 
    while True:
        if arr[m] == 1:
            print(m)
            union(red_card, m)
            arr[m] = 0
            break
        else:
            union(red_card, m)
            m = p[m]

            
    
    
#
# 7 6 6
# 2 3 4 5 6 7
# 1 4 2 5 2 5

# 7 6 6
# 2 3 4 5 6 7
# 4 3 2 1 1 1