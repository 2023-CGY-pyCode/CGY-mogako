li = []

for _ in range(5):
    a = list(map(int, input().split()))
    li.append(a)
    
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


s = set()
def dfs(x,y, trace=''):
    # if visited[x][y]:
    #     return
    if len(trace) == 6:
        s.add(trace)
    else:
        # visited[x][y] = True
        trace += str(li[x][y])
    
        for i in range(4):
            if x+dx[i] >= 0 and x+dx[i] <= 4 and y+dy[i] >= 0 and y+dy[i] <= 4:
                dfs(x+dx[i], y+dy[i], trace)
            

for x in range(5):
    for y in range(5):
        # visited = [[False]*5 for _ in range(5)]
        dfs(x, y, '')
        
print(len(s))
    
    