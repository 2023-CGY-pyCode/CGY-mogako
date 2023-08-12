import sys
input = sys.stdin.readline

# Test Case


T = int(input())

stack = list()
visited = [0] * (1001)
def dfs_sort(graphs, curr, W):
    visited[curr] = 1
    
    for node in graphs[curr]:
        if visited[node] == 0:
            visited[node] = 1
            print(node)
            dfs_sort(graphs, node, W)
            
    stack.append(curr)


for _ in range(T):
    # Building, Rules Counts
    N, K = map(int, input().split()) 
    visited = [0] * (1001)
    dp = [0] * (N+1)
    
    graphs = [[] * (N+1) for _ in range(N+1)]
    ans = [0] * (N+1)
    roles = [0] * (N+1)
    li = list(map(int, input().split()))
    # rules input
    for i in range(1, N+1): 
        roles[i] = li[i-1]
        

    for i in range(K):
        
        X, Y = tuple(map(int, input().split()))
        graphs[X].append(Y)

    for i in range(1, N+1):
        graphs[0].append(i) # 모든 정점을 연결하는 0배열
        
    W = int(input())
    
    # W 기준으로 위상정렬
    dfs_sort(graphs, 0, W)
    print("stack", stack)
    # dp[graphs[0][0]] = rules[graphs[0][0]]
    
    stack.pop() # 0 제거
    dp[stack[-1]] = roles[stack[-1]] 
    
    while stack:
        X = stack.pop()
        if (X == W):
            continue
        for i in graphs[X]:
            dp[i] = max(dp[i], dp[X]+roles[i])
        
    
    print(dp)
    print("출력은:", dp[W]) # target DP

    
        
    
       
