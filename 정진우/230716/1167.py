import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())
tree = [[] for _ in range(n+1)]
# print(tree)

for _ in range(n):
    li = list(map(int, input().split()))
    e = li[0]
    if li[1] == -1:
        continue
    for i in range(1, len(li)-1, 2):
        v, c = li[i], li[i+1]
        tree[e].append((v,c))
    
print(tree)
dfs_list = []
def dfs(s, e, result):
    for u, v in tree[s]:
        if u != e:
            target, cost = dfs(u, s, result+v)
            dfs_list.append((target,cost))
    return s, result

dfs(1, 1, 0)
dfs_list.sort(key=lambda x: x[1], reverse=True)
# print(dfs_list)
start, _ = dfs_list[0]

dfs_list.clear()
dfs(start, start, 0)

dfs_list.sort(key=lambda x: x[1], reverse=True)
print(dfs_list[0][1])
            
    





    
