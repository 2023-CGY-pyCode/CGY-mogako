import sys
input = sys.stdin.readline

N = int(input())

inf = ans = 1e9

cost = []

for _ in range(N):
    cost.append(list(map(int, input().split()))) # RGB 거리 넣어주기

for c in range(3):    
    dp = [[0] * 3 for _ in range(N)]
    
    dp[0] = [inf, inf, inf]
    dp[0][c] = cost[0][c] 
    
    for i in range(1, N):
        dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + cost[i][0]
        dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + cost[i][1]
        dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + cost[i][2]
    
    dp[N-1][c] = inf
    ans = min(ans, min(dp[N-1]))
    
print(ans)
    
    
    