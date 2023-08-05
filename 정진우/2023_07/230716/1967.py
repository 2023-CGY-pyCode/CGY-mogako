import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)


n = int(input())
tree = [[] for _ in range(n+1)]
# print(tree)

for _ in range(n-1):
    e, v, c = tuple(map(int, input().split()))
    tree[e].append((v,c))
    tree[v].append((e,c))
    
    
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
if n != 1:
    start, _ = dfs_list[0]

    dfs_list.clear()
    dfs(start, start, 0)

    dfs_list.sort(key=lambda x: x[1], reverse=True)
    print(dfs_list[0][1])
else:
    print(0)
            
    





    
