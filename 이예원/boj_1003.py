import sys

t = int(sys.stdin.readline())
dp = [0] * 41
dp[0], dp[1] = [1, 0], [0, 1]
for _ in range(t):
    n = int(sys.stdin.readline())
    for i in range(2, n+1):
        dp[i] = list(dp[i-1][j] + dp[i-2][j] for j in range(2))
    print(dp[n][0], dp[n][1])