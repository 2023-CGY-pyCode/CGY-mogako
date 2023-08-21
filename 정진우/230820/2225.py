N, K = map(int, input().split())

dp = [[1] * (N+1) for _ in range(K+1)]

# dp[k][n] = dp[k][n-1] + dp[k-1][n]

for i in range(2, K+1):
    for j in range(1, N+1):
        dp[i][j] = (dp[i][j-1] + dp[i-1][j]) % int(1e9)
        
print(dp[K][N])